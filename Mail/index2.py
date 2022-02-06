import pandas as pd
import smtplib
import numpy as np
import os
import time
import smtplib
from ssl import create_default_context
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders


data = pd.read_excel('./calling_list.xlsx')
name = pd.DataFrame(data, columns=['Name'])
comment = pd.DataFrame(data, columns=['Comments'])
email = pd.DataFrame(data, columns=['Email'])


#     print(name.iloc[i, 0])
#     username = (name.iloc[i, 0])
#     print(email.iloc[i, 0])
#     sender = 'ravikishan63392@gmail.com'
#     receivers = [email.iloc[i, 0]]


mail_content = '''
<html>

<head>
<meta http-equiv=Content-Type content="text/html; charset=utf-8">
<meta name=Generator content="Microsoft Word 15 (filtered)">
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:Mangal;
	panose-1:0 0 4 0 0 0 0 0 0 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;}
@font-face
	{font-family:Verdana;
	panose-1:2 11 6 4 3 5 4 4 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:8.0pt;
	margin-left:0in;
	line-height:107%;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif;}
.MsoChpDefault
	{font-family:"Calibri",sans-serif;}
.MsoPapDefault
	{margin-bottom:8.0pt;
	line-height:107%;}
@page WordSection1
	{size:595.3pt 841.9pt;
	margin:1.0in 1.0in 1.0in 1.0in;}
div.WordSection1
	{page:WordSection1;}
-->
</style>

</head>

<body lang=EN-US link=blue vlink="#954F72" style='word-wrap:break-word'>

<div class=WordSection1>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>Dear Ma'am/Sir,&nbsp;</span></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;background:white'><span lang=EN-IN style='font-size:12.0pt;font-family:
"Times New Roman",serif;color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;background:white'><b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>Greetings!!!!</span></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;background:white'><span lang=EN-IN style='font-size:12.0pt;font-family:
"Times New Roman",serif;color:black'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;background:white'><span lang=EN-IN style='font-size:12.0pt;font-family:
"Times New Roman",serif;color:black'>We feel immense pleasure in inviting you
to Prestige Institute of Management &amp; Research, Gwalior&nbsp;</span><b><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>(UGC approved, Autonomous, UGC-NAAC Accredited ‘A’ grade and NBA
Accredited Institute)</span></i></b></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>&nbsp;</span></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:blue'>13<sup>th</sup><u>&nbsp;PIMR-G International
Conference on&nbsp;</u></span></b></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><b><u><span lang=EN-IN style='font-size:
12.0pt;font-family:"Times New Roman",serif;color:blue'>Industry 4.0 &amp; Key
Drivers of Sustainable Global Business&nbsp;Practices (ICSGBP) -&nbsp;<i>Hybrid
Mode</i></span></u></b></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><span lang=EN-IN style='color:#222222'>&nbsp;</span></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><b><i><u><span lang=EN-IN
style='font-size:12.0pt;font-family:"Times New Roman",serif;color:blue'>in
association with AIBPM, Indonesia</span></u></i></b></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><span lang=EN-IN style='color:#222222'>&nbsp;</span></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:blue'>organized by</span></b></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:blue'>&nbsp;</span></b></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><b><span lang=EN-IN style='font-size:13.5pt;
font-family:"Times New Roman",serif;color:blue'>Prestige Institute of
Management &amp; Research Gwalior during</span></b></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:blue'>&nbsp;</span></b></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:normal;background:white'><b><span lang=EN-IN style='font-size:20.0pt;
font-family:"Times New Roman",serif;color:blue;background:yellow'>January 08-10,
2022</span></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><u><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>Major Attractions of the Conference:</span></u></b></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#500050'>&nbsp;</span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>1.&nbsp;</span></b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>Publication&nbsp;Opportunities
for participants in high index journals like;<b>&nbsp;“Scopus, Web of Sciences
&amp; ABDC</b>&nbsp;<b>listed&quot;</b>.</span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>2.&nbsp;</span></b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>The selected papers will have
opportunity&nbsp;for&nbsp;publication after double blind peer review in&nbsp;<b>Sanchayan-PJMIT</b></span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>3.&nbsp;</span></b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>The remaining papers will be
published in one edited volume with ISBN Number after review</span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>4.&nbsp;</span></b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>“<b>The Best Thesis Award</b>”
(Cash Prize) (only for the participants who have been awarded their Ph.D.
between January 2016- September 2021).</span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>5.&nbsp;</span></b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>&quot;<b>Best Paper Award</b>&quot;
Separate Track for presentation (Cash Prize)&nbsp;and opportunity to&nbsp;<b>Publish
in High Index Journal</b></span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>6. Panel Discussion&nbsp;</span></b><span lang=EN-IN
style='font-size:12.0pt;font-family:"Times New Roman",serif;color:black'>on
Industry 4.0: Current &amp; Future Trends.</span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
14.65pt;background:white'><b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>&nbsp;</span></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
14.65pt;background:white'><b><u><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>Publication Opportunities:</span></u></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
14.65pt;background:white'><b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>&nbsp;</span></b></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>1.</span><span lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span lang=EN-IN
style='font-size:12.0pt;font-family:"Times New Roman",serif;color:black'>Selected
Papers will be published (after peer review) in the Special issue of
International Journal of Professional Business Review.</span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>2.</span><span lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span lang=EN-IN
style='font-size:12.0pt;font-family:"Times New Roman",serif;color:black'>Selected
Papers will be published (after peer review) in the following&nbsp;<b>(Scopus
listed &amp; Inderscience published Journals)</b></span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:Symbol;color:black'>·</span><span
lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>International Journal of Globalization and Small Business</span></i></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:Symbol;color:black'>·</span><span
lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>World Review of Entrepreneurship, Management and Sustainable
Development</span></i></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:Symbol;color:black'>·</span><span
lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>International Journal of Technology Transfer and Commercialization</span></i></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:Symbol;color:black'>·</span><span
lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>International Journal of Public Sector Performance Management</span></i></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:Symbol;color:black'>·</span><span
lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>FIIB Business Review</span></i></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:Symbol;color:black'>·</span><span
lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>International Journal of Professional Business Review</span></i></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:Symbol;color:black'>·</span><span
lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>Journal of Content, Community &amp; Communication</span></i></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>3.</span><span lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span lang=EN-IN
style='font-size:12.0pt;font-family:"Times New Roman",serif;color:black'>The
selected papers will have opportunity for publication after double blind peer
review in Sanchayan-PJMIT</span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.5in;text-align:justify;line-height:14.65pt;background:white'><span
lang=EN-IN style='font-size:13.5pt;font-family:"Verdana",sans-serif;color:black'>4.</span><span
lang=EN-IN style='font-size:7.0pt;font-family:"Times New Roman",serif;
color:black'>&nbsp;&nbsp;</span><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>&nbsp;The remaining papers
will be published in one edited volume with ISBN Number after review.</span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;background:white'><span lang=EN-IN style='font-size:12.0pt;font-family:
"Times New Roman",serif;color:black'>All the submitted papers will have the
opportunity to be presented&nbsp;during the conference.&nbsp;The selected
papers will be considered for publication after a&nbsp;<b><i>proper peer review
process</i></b>.</span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;background:white'><span lang=EN-IN style='font-size:12.0pt;font-family:
"Times New Roman",serif;color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;background:white'><span lang=EN-IN style='font-size:12.0pt;font-family:
"Times New Roman",serif;color:black'>We also request you to motivate your
colleagues and scholars to attend this workshop and circulate/forward this
communication among your colleagues and scholars.</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:black'>SUBMIT ARTICLES ON:&nbsp;</span></b><span lang=EN-IN
style='color:black'><a href="mailto:ICSGBP@PRESTIGEGWL.ORG" target="_blank"><b><span
style='font-size:12.0pt;font-family:"Times New Roman",serif'>ICSGBP@PRESTIGEGWL.ORG</span></b></a></span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>&nbsp;</span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=359 valign=top style='width:269.1pt;border:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:#500050'>Important Dates</span></b></p>
  </td>
  <td width=218 valign=top style='width:163.7pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:#500050'>Dates</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=359 valign=top style='width:269.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#FBE4D5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
  normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
  color:black'>Last Date for Submission of Abstract</span></b></p>
  </td>
  <td width=218 valign=top style='width:163.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FBE4D5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>November 30, 2021</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=359 valign=top style='width:269.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
  normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
  color:black'>Last Date for Submission of Full Paper</span></b></p>
  </td>
  <td width=218 valign=top style='width:163.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>December 15, 2021</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=359 valign=top style='width:269.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#FBE4D5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
  normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
  color:black'>Notification of Acceptance of Full Paper</span></b></p>
  </td>
  <td width=218 valign=top style='width:163.7pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#FBE4D5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>December 25, 2021</span></b></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>&nbsp;</span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width=678
 style='width:508.25pt;border-collapse:collapse'>
 <tr style='height:15.0pt'>
  <td width=678 nowrap colspan=5 valign=bottom style='width:508.25pt;
  border:solid windowtext 1.0pt;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Registration Fees</span></b></p>
  </td>
 </tr>
 <tr style='height:38.25pt'>
  <td nowrap style='border:solid windowtext 1.0pt;border-top:none;padding:.75pt .75pt 0in .75pt;
  height:38.25pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Delegate Category (Non-residential)</span></b></p>
  </td>
  <td width=85 style='width:64.05pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:.75pt .75pt 0in .75pt;height:38.25pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Online</span></b></p>
  </td>
  <td width=90 style='width:67.5pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:.75pt .75pt 0in .75pt;
  height:38.25pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Offline</span></b></p>
  </td>
  <td width=96 style='width:1.0in;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;background:yellow;
  padding:.75pt .75pt 0in .75pt;height:38.25pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Registration Fees in US $</span></b></p>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Online</span></b></p>
  </td>
  <td width=102 style='width:76.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:0in 0in 0in 0in;height:38.25pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Registration Fees in US $</span></b></p>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><b><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Offline</span></b></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td nowrap valign=bottom style='border:solid windowtext 1.0pt;border-top:
  none;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><span
  lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
  color:black'>Business Executive &amp; Academicians (Faculty)</span></p>
  </td>
  <td width=85 valign=bottom style='width:64.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Rs. 3500/-</span></p>
  </td>
  <td width=90 nowrap valign=bottom style='width:67.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Rs. 4500/-</span></p>
  </td>
  <td width=96 nowrap valign=bottom style='width:1.0in;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>$200/-</span></p>
  </td>
  <td width=102 valign=bottom style='width:76.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:0in 0in 0in 0in;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>$250/-</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td nowrap valign=bottom style='border:solid windowtext 1.0pt;border-top:
  none;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><span
  lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
  color:black'>Research Scholars (Doctoral/Post-Doctoral)</span></p>
  </td>
  <td width=85 valign=bottom style='width:64.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Rs. 2500/-</span></p>
  </td>
  <td width=90 nowrap valign=bottom style='width:67.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Rs. 3500/-</span></p>
  </td>
  <td width=96 nowrap valign=bottom style='width:1.0in;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>$150/-</span></p>
  </td>
  <td width=102 valign=bottom style='width:76.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:0in 0in 0in 0in;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>$180/-</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td nowrap valign=bottom style='border:solid windowtext 1.0pt;border-top:
  none;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><span
  lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
  color:black'>Regular Students</span></p>
  </td>
  <td width=85 valign=bottom style='width:64.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Rs. 2000/-</span></p>
  </td>
  <td width=90 nowrap valign=bottom style='width:67.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>Rs. 3000/-</span></p>
  </td>
  <td width=96 nowrap valign=bottom style='width:1.0in;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:.75pt .75pt 0in .75pt;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>$50/-</span></p>
  </td>
  <td width=102 valign=bottom style='width:76.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:yellow;padding:0in 0in 0in 0in;height:15.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
  line-height:normal'><span lang=EN-IN style='font-size:12.0pt;font-family:
  "Times New Roman",serif;color:black'>$70/-</span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>Note: Best Thesis registration is same as of academicians.</span></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><u><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>Modes of Payment:</span></u></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:#500050'>&nbsp;</span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=180 valign=top style='width:134.75pt;border:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN style='color:black'>Account No.</span></b></p>
  </td>
  <td width=246 valign=top style='width:184.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>0328002100028783</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=180 valign=top style='width:134.75pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>Bank / IFSC</span></b></p>
  </td>
  <td width=246 valign=top style='width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>Punjab National Bank/PUNB 0032800</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=180 valign=top style='width:134.75pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>Bank Branch/ Branch Code</span></b></p>
  </td>
  <td width=246 valign=top style='width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>Mall Road, Morar, Gwalior/ Code:24</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=180 valign=top style='width:134.75pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>MICR Code</span></b></p>
  </td>
  <td width=246 valign=top style='width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>474024006</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=180 valign=top style='width:134.75pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>PAYTM Can be done at</span></b></p>
  </td>
  <td width=246 valign=top style='width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>98276 62240 (QR below)</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=180 valign=top style='width:134.75pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>DD in Favor of</span></b></p>
  </td>
  <td width=246 valign=top style='width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><b><span
  lang=EN-IN>“Prestige Institute of Management”</span></b></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='line-height:11.75pt;background:white'><span
lang=EN-IN style='color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;background:white'><b><span lang=EN-IN style='font-size:12.0pt;
font-family:"Times New Roman",serif;color:black'>Early Bird Registration can
avail a discount of 10% in registration fees valid only before December 15<sup>th</sup>&nbsp;2021.</span></b></p>

<p class=MsoNormal style='background:white'><b><span lang=EN-IN
style='font-size:12.0pt;font-family:"Times New Roman",serif;color:black'>*<span
style='background:yellow'>Group discount can be availed. The discount will be
10% for 2 delegates, 15% for 3 delegates, 20% for 4 or more delegates.</span></span></b></p>

<p class=MsoNormal style='background:white'><b><span lang=EN-IN
style='font-size:12.0pt;font-family:"Times New Roman",serif;color:black;
background:yellow'>&nbsp;</span></b></p>

<p class=MsoNormal style='text-align:justify;line-height:11.75pt;background:
white'><b><span lang=EN-IN style='color:black'>PAYTM AT</span></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='color:black'>Enclosed is Paytm QR Code </p>
<p class=MsoNormal style='text-align:justify;line-height:11.75pt;background:
white'><span lang=EN-IN style='color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='text-align:justify;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Times New Roman",serif;
color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='text-align:justify;line-height:11.75pt;background:
white'><b><span lang=EN-IN style='color:black'>REGISTRATION FORM</span></b></p>

<p class=MsoNormal style='text-align:justify;line-height:11.75pt;background:
white'><span lang=EN-IN style='color:black'><a
href="https://forms.gle/yJ7cbmtm1Vrgw1bZ7" target="_blank"><span
style='color:#1155CC'>https://forms.gle/yJ7cbmtm1Vrgw1bZ7</span></a></span><span
lang=EN-IN style='color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='text-align:justify;line-height:11.75pt;background:
white'><b><i><span lang=EN-IN style='color:#222222'>Click here for Brochure:</span></i></b></p>

<p class=MsoNormal style='line-height:11.75pt;background:white'><span
lang=EN-IN style='color:black'><a
href="https://www.prestigegwl.org/all_upcoming_events.php" target="_blank"><span
style='color:#1155CC'>https://www.prestigegwl.org/all_upcoming_events.php<br
clear=all>
</span></a></span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><span
lang=EN-GB style='font-size:13.0pt;font-family:"Times New Roman",serif;
color:blue'>Prof. (Dr.) Navita Nathani&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Dr. Indira
Sharma&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Asst. Prof. B N Sharma &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-GB style='font-size:13.5pt;font-family:"Times New Roman",serif;
color:blue'>Conference Convenor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Organizing
Secretary&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Co-Organizing Secretary</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:13.5pt;font-family:"Times New Roman",serif;
color:blue'>+91.9826440388&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
+91.9926070125&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
+91.78277704208</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='color:black'><a href="mailto:drnavita@prestigegwl.org"
target="_blank"><span lang=EN-GB style='font-family:"Times New Roman",serif'>drnavita@prestigegwl.org</span></a></span><span
lang=EN-GB style='font-family:"Times New Roman",serif;color:blue'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span
lang=EN-IN style='color:black'><a href="mailto:indira.sharma@prestigegwl.org"
target="_blank"><span lang=EN-GB style='font-family:"Times New Roman",serif'>indira.sharma@prestigegwl.org</span></a></span><span
lang=EN-GB style='font-family:"Times New Roman",serif;color:blue'>&nbsp;</span><span
lang=EN-IN style='color:black'><a
href="mailto:brahmmanand.sharma@prestigegwl.org" target="_blank"><span
lang=EN-GB style='font-family:"Times New Roman",serif'>brahmmanand.sharma@prestigegwl.org</span></a></span><span
lang=EN-GB style='font-family:"Times New Roman",serif;color:blue'>&nbsp;&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-family:"Times New Roman",serif;color:blue'><br
clear=all>
</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:blue'>Thanks
&amp; Regards,</span></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:blue'>Dr.
Indira Sharma</span></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:blue'>Faculty
(HR &amp; OB)</span></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:blue'>13th
PIMRG International Conference Organizing Secretary&nbsp;</span></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:blue'>Prestige
Institute of Management Gwalior</span></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:blue'>+919926070125</span></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><b><i><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:blue'>+919340078072</span></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:#222222'>&nbsp;</span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;background:white'><span
lang=EN-IN style='font-size:12.0pt;font-family:"Arial",sans-serif;color:#222222'>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-IN>&nbsp;</span></p>

</div>

</body>

</html>

<!-- image at 665 -->
'''


receiver_address = []
'''print each value in dataframe'''
for i in range(len(name)):
        if(comment.iloc[i, 0]) == "gmail":
                recive_ad = email.iloc[i, 0]
                receiver_address.append(recive_ad)
                print(receiver_address)

sender_address = 'indiraraosharma@gmail.com'
sender_pass = ''
message = MIMEMultipart()
message['From'] = sender_address
# message['To'] = receiver_address
message['Subject'] = '13th PIMRG International Conference - SCOPUS Publication Opportunity'
                #The subject line
                #The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'html'))
attach_file_name = 'FINAL IC BROCHURE (1).pdf'
attach_file_name2 = 'paytm.png'
with open(attach_file_name,'rb') as file:
        message.attach(MIMEApplication(file.read(), Name=attach_file_name))
with open(attach_file_name2,'rb') as file2:
        message.attach(MIMEApplication(file2.read(), Name=attach_file_name2))
session = smtplib.SMTP(host='smtp.gmail.com',port=587) #use gmail with port
session.starttls(context=create_default_context()) #enable security
session.ehlo()
session.login(sender_address, sender_pass)
text = message.as_string()
to = ", ".join(receiver_address)
session.sendmail(sender_address, to, text)
session.quit()
print('Mail Sent')
