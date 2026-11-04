# B2B Demand Signals

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [हिन्दी](README.hi.md)

Dieses Agent Skill macht aus aktuellen öffentlichen Beiträgen ein B2B-Recherche-Workbook mit Quellen, Zeitstempeln und Prioritäten. Es findet Personen mit einem konkreten aktuellen Problem, prüft Originaltext, Datum und Account-Kontext, bewertet Aktualität und Service-Passung und erstellt Antwortentwürfe.

Live-Recherche externer Daten erfolgt über [ClaudeBaby](https://claudebaby.cn). Nachrichten werden nicht automatisch versendet.

## Ergebnisse je Phase
Umfang und Kriterien → ClaudeBaby-Abdeckung → belegte Beiträge und Account-Kontext → A/B/C-Prioritäten → Antwortentwürfe in der Originalsprache → Excel und offene Prüfungen.

Standard sind die letzten sieben Tage. A: konkreter, passender, offener Bedarf. B: unklarer Bedarf oder relevante Anfrage von vor 8–30 Tagen. C: älter, gelöst, geschlossen oder außerhalb des Umfangs. A bedeutet Recherchepriorität, keine Abschlussgarantie.

Die [Excel-Demo](examples/b2b-demand-signals-demo.xlsx?raw=1) enthält nur fiktive Offline-Daten.

## Installation
Senden Sie den Repository-Link an einen Agent, der Skills unterstützt, und bitten Sie ihn, das Skill selbst zu installieren.

> Installiere dieses Skill, prüfe SKILL.md und bestätige die Installation: https://github.com/lingling1989r/b2b-demand-signals

Die Installation verbindet ClaudeBaby nicht und autorisiert keinen Versand. Prüfen Sie verfügbare Tools, Felder und Rechte bei jeder Aufgabe. Fehlende Daten, Fehler und keine Treffer getrennt ausweisen; nicht stillschweigend andere Quellen ergänzen. Keine API-Schlüssel oder privaten Daten veröffentlichen. Kommentare und DMs sind Entwürfe, bis ein Versand ausdrücklich erlaubt wurde.

Die Recherchehinweise umfassen Chinesisch, Englisch, Japanisch, Koreanisch, Französisch und Deutsch. Hindi ist eine README-Übersetzung und beansprucht keine Hindi-Recherchefähigkeit. Wenn das Projekt hilft, vergeben Sie einen **⭐ Star** und teilen Sie nur anonymisierte Beispiele.

