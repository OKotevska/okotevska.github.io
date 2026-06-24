#!/usr/bin/env python3
"""Check HTTP status of high-risk external links."""
import urllib.request, urllib.error, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    ("CVENT WP-1 (DOE ASCR)", "https://custom.cvent.com/DCBD4ADAAD004096B1E4AD96F3C8049E/files/event/f9a6d32df34c43e5980b54f79ad848bc/738372bbcdd246ac9a9c00a177c075ac.pdf"),
    ("CVENT WP-2 (DOE ASCR)", "https://custom.cvent.com/DCBD4ADAAD004096B1E4AD96F3C8049E/files/event/f9a6d32df34c43e5980b54f79ad848bc/2e42c4c5dbe74b578e47188036244a10.pdf"),
    ("IIoT Cities 2022 speaker", "https://cities2022.iiotday.com/speaker/olivera-kotevska/"),
    ("Smart Regions 2018", "https://smartregionsconference2018.sched.com/event/GuQN/safety-and-security-in-smart-cities-and-regions-forum"),
    ("ANL event page", "https://www.anl.gov/event/privacy-algorithms-current-developments-and-future-directions"),
    ("IEEE R3 newsletter", "https://r3.ieee.org/2022/06/13/newsletter-volume-36-no-2/"),
    ("IEEE CAI conf", "https://ieee-cai.org/"),
    ("CIKM 2022 conf", "https://www.cikm2022.org/"),
    ("AI4ESP PDF", "https://ai4esp.org/files/AI4ESP1111_Rastogi_Deeksha.pdf"),
    ("IOTBDS tutorial 2021", "https://iotbds.scitevents.org/Tutorials.aspx?y=2021"),
    ("CIIT 2011 PDF", "http://ciit.finki.ukim.mk/data/papers/8CiiT/8CiiT-09.pdf"),
    ("ICRA-SEA 2026 (.top domain)", "https://www.2026-ieee-icra-sea.top"),
    ("energyconsequences.com", "https://www.energyconsequences.com"),
    ("NOAA workshop 2020", "https://www.star.nesdis.noaa.gov/star/meeting_2020AIWorkshop_agenda.php"),
    ("Tapia 2018 PDF", "https://tapiaconference.cmd-it.org/wp-content/uploads/2020/06/Tapia-Conference-2018-Program.pdf"),
    ("TPC 2026 breakout", "https://tpc26.org/tpc-agenda-breakout-groups/"),
    ("IEEE Region 6 talk", "https://ieee-region6.org/event/privacy-algorithms-research-practice-and-transfer-to-industry-3/"),
    ("eprints UGD 2013", "http://eprints.ugd.edu.mk/8757/"),
]

print(f"{'STATUS':<8} {'LABEL'}")
print("-" * 70)
for label, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            print(f"  {r.status:<6} {label}")
    except urllib.error.HTTPError as e:
        print(f"  {e.code:<6} {label}  ** CHECK **")
    except Exception as e:
        print(f"  {'ERR':<6} {label}  ** {type(e).__name__} **")
    time.sleep(0.3)
