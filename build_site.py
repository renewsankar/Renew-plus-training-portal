"""Rebuilds index.html, sitemap.xml and robots.txt from the files in docs/ and videos/.
Run:  python3 build_site.py https://YOUR-USERNAME.github.io/renew-plus-training-portal/
"""
import json, os, subprocess, sys

SITE = (sys.argv[1] if len(sys.argv) > 1 else 'https://YOUR-USERNAME.github.io/renew-plus-training-portal/').rstrip('/') + '/'
ROOT = os.path.dirname(os.path.abspath(__file__))

ITEMS = [
 dict(id='orientation', docno='RP-TRN-001', cat='staff', tag='Staff Onboarding', title='Employee Orientation Guide', pdf='Renew_Plus_Employee_Orientation_Guide_v1.1',
      desc='Roles, responsibilities, daily rhythm, reporting line and the patient journey for every new branch employee.',
      index=[(1, 'Cover'), (2, 'Welcome & reporting structure'), (3, 'Daily rhythm & working hours'), (4, 'The patient journey'),
             (5, 'Role: Branch Manager'), (6, 'Role: Doctors (Hair & Skin)'), (7, 'Role: Nurse'), (8, 'Role: Tele Caller'),
             (9, 'Role: Front Office Executive'), (10, 'Role: Admin'), (11, 'Orientation acknowledgement')]),
 dict(id='telecaller', docno='RP-TRN-002', cat='staff', tag='Staff Training', title='Telecaller Training', video='Renew_Plus_Telecaller_Training_Video',
      desc='Our company, clinics, hair, skin and slimming services, the five-step call flow, scripts, objections and call quality.'),
 dict(id='service', docno='RP-TRN-003', cat='staff', tag='Staff Training', title='Service Training Manual', pdf='Renew_Plus_Service_Training_Manual', video='Renew_Plus_Service_Training_Video',
      desc='Hydra facial, chemical peels, microneedling and skin boosters — indications, procedure steps, safety and aftercare.',
      index=[(1, 'Cover'), (2, 'Contents & welcome'), (3, 'Part A · Hydra Facial'), (5, 'Part B · Chemical Peels'), (7, 'Rinse-off & retinol peel SOPs'),
             (8, 'Part C · Microneedling'), (9, 'Part D · Skin Boosters'), (10, 'Product classes & brands'), (14, 'Adverse events & emergencies'),
             (15, 'Part E · Records & client template'), (16, 'References'), (17, 'Trainee acknowledgement')]),
 dict(id='sop', docno='RP-OPS-001', cat='ops', tag='Clinic Operations', title='Clinic SOP Handbook', pdf='Renew_Plus_Clinic_SOP_Handbook', video='Renew_Plus_Clinic_SOP_Handbook_Video',
      desc='Standard operating procedures for all branches: reception, consultation, consent, procedures, infection control, emergencies and audits.',
      index=[(1, 'Cover'), (2, 'Document control & contents'), (3, 'Purpose, scope & roles'), (4, 'Patient journey map'), (5, 'Touchpoints & front desk'),
             (6, 'Appointments, registration & billing'), (7, 'Consultation & hair assessment'), (8, 'Skin assessment & consent'), (9, 'Consent checklist & hair SOP'),
             (10, 'PRP & hair restoration'), (11, 'Skin procedures, peels & lasers'), (12, 'Aftercare & infection control'), (13, 'Sterilisation & emergency handling'),
             (14, 'Emergency readiness & records'), (15, 'Photography & complaints'), (16, 'Opening & closing checklists'), (17, 'Branch audit'),
             (18, 'Document control & approvals'), (19, 'SOP acknowledgement')]),
 dict(id='beforeafter', docno='RP-CLN-001', cat='clinical', tag='Clinical Documentation', title='Before & After Case Handbook', pdf='Renew_Plus_Before_After_Case_Handbook', video='Renew_Plus_Before_After_Case_Handbook_Video',
      desc='Case pages for hair and skin treatments, the clinical photography standard, consent checklist and case record.',
      index=[(1, 'Cover'), (2, 'About & contents'), (3, '01 · Hair case index'), (4, 'FUE Hair Transplant'), (6, 'DHI Hair Transplant'), (8, 'Sapphire Hair Transplant'),
             (10, 'GFC Hair Treatment'), (12, 'PRP Hair Treatment'), (14, 'Mesotherapy'), (16, 'QR678'), (18, 'Hair Fall / Thinning'), (20, '02 · Skin case index'),
             (21, 'Acne'), (22, 'Acne Scar'), (23, 'Pigmentation'), (24, 'Q-Switch Laser'), (25, 'Chemical Peel'), (26, 'HydraFacial'), (27, 'Dermaplaning'),
             (28, 'Carbon Laser'), (29, 'Skin Rejuvenation'), (30, 'Anti-Ageing'), (31, 'Lip Pigmentation'), (32, 'Laser Hair Removal'), (33, 'Keloid / Scar Care'),
             (34, 'IV Glutathione'), (35, '03 · Photography standard'), (36, '04 · Consent & case record'), (37, 'Contact')]),
 dict(id='hair', docno='RP-PAT-001', cat='patient', tag='Patient Care', title='Hair Treatment Aftercare', pdf='Renew_Plus_Hair_Treatment_Aftercare', video='Renew_Plus_Hair_Treatment_Aftercare_Video',
      desc="Do's and don'ts after hair restoration and hair fall treatments, and when to contact the clinic.",
      index=[(1, 'Cover'), (2, "Do's"), (3, "Don'ts"), (4, 'When to seek help'), (5, 'Your recovery')]),
 dict(id='skin', docno='RP-PAT-002', cat='patient', tag='Patient Care', title='Skin Treatment Aftercare', pdf='Renew_Plus_Skin_Treatment_Aftercare', video='Renew_Plus_Skin_Treatment_Aftercare_Video',
      desc="Do's and don'ts after facials, peels, laser and skin rejuvenation, with treatment-specific reminders.",
      index=[(1, 'Cover'), (2, "Do's"), (3, "Don'ts"), (4, 'Treatment-specific care'), (5, 'When to seek help'), (6, 'Your recovery')]),
]


def mb(path):
    return f'{os.path.getsize(path) / 1048576:.1f} MB'


CHAPTERS = json.load(open(os.path.join(ROOT, 'chapters.json'), encoding='utf-8'))
for it in ITEMS:
    if 'pdf' in it:
        it['pdfNo'] = it['docno'] + '-D'
    if 'video' in it:
        it['vidNo'] = it['docno'] + '-V'
        it['chapters'] = CHAPTERS[it['video']]
        for n in range(1, len(it['chapters']) + 1):
            assert os.path.exists(os.path.join(ROOT, 'assets', 'chapters', it['video'], f'{n}.jpg')), (it['video'], n)
    if 'pdf' in it:
        p = os.path.join(ROOT, 'docs', it['pdf'] + '.pdf')
        out = subprocess.run(['pdfinfo', p], capture_output=True, text=True).stdout
        it['pages'] = int([l for l in out.splitlines() if l.startswith('Pages:')][0].split()[1])
        it['pdfSize'] = mb(p)
        for pg, _ in it['index']:
            assert os.path.exists(os.path.join(ROOT, 'assets', 'pages', it['pdf'], f'{pg}.jpg')), (it['pdf'], pg)
    if 'video' in it:
        v = os.path.join(ROOT, 'videos', it['video'] + '.mp4')
        d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', v], capture_output=True, text=True).stdout)
        it['dur'] = f'{int(d // 60)}:{int(round(d % 60)):02d}'
        it['vidSize'] = mb(v)

tpl = open(os.path.join(ROOT, 'template.html'), encoding='utf-8').read()
html = tpl.replace('__ITEMS__', json.dumps(ITEMS, ensure_ascii=False)).replace('__SITE__', SITE)
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(html)

urls = [SITE] + [SITE + 'docs/' + i['pdf'] + '.pdf' for i in ITEMS if 'pdf' in i]
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n')
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
print('Built index.html for', SITE, '-', len(ITEMS), 'items')
