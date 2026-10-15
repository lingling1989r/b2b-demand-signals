import datetime as dt
import importlib.util
from pathlib import Path
import unittest
from zoneinfo import ZoneInfo

spec = importlib.util.spec_from_file_location('grader', Path(__file__).parents[1] / 'scripts/grade_signals.py')
grader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grader)


class FreshnessTests(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime.fromisoformat('2026-10-15T18:00:00+08:00')
        self.zone = ZoneInfo('Asia/Shanghai')

    def classify(self, **patch):
        row = dict(lead_id='demo', published_at='2026-10-14T10:00:00+08:00',
                   demand_strength='explicit', service_fit='direct')
        row.update(patch)
        value = grader.grade(row, self.now, self.zone)
        return value['grade'], value['bucket']

    def test_freshness_changes_placement(self):
        self.assertEqual(self.classify(), ('A', 'recent_workbench'))
        self.assertEqual(self.classify(published_at='2026-10-01T10:00:00+08:00'), ('B', 'historical_candidates'))
        self.assertEqual(self.classify(published_at='2026-08-01T10:00:00+08:00'), ('C', 'archive'))

    def test_closed_overrides_freshness(self):
        self.assertEqual(self.classify(closed=True), ('C', 'excluded'))
        self.assertEqual(self.classify(account_inactive=True), ('C', 'excluded'))

    def test_general_or_indirect_not_a(self):
        self.assertEqual(self.classify(demand_strength='general')[0], 'B')
        self.assertEqual(self.classify(service_fit='indirect')[0], 'B')

    def test_missing_or_future_dates_do_not_become_recent(self):
        self.assertEqual(self.classify(published_at=None), ('B', 'date_pending'))
        self.assertEqual(self.classify(published_at='2026-10-16T10:00:00+08:00'), ('C', 'date_pending'))
        self.assertEqual(self.classify(published_at='2026-10-14T10:00:00'), ('C', 'date_pending'))

    def test_exact_and_date_only_boundaries(self):
        self.assertEqual(self.classify(published_at='2026-10-08T18:00:00+08:00')[0], 'A')
        self.assertEqual(self.classify(published_at='2026-10-08'), ('B', 'date_pending'))
        self.assertEqual(self.classify(published_at='2026-10-14')[0], 'A')

    def test_timezone_equivalence(self):
        self.assertEqual(self.classify(published_at='2026-10-14T02:00:00Z'), self.classify())

    def test_invalid_labels_and_string_boolean_rejected(self):
        for patch in [dict(closed='false'), dict(service_fit='maybe'), dict(demand_strength='hot')]:
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                self.classify(**patch)


if __name__ == '__main__':
    unittest.main()
