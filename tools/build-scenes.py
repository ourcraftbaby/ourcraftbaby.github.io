"""Draws the three landscape scenes and writes ../index.html from index.template.html.
Edit the page text in the template and the drawings here, then run:  python tools/build-scenes.py"""
import os, random
random.seed(7)

PINE = "M0 0l-10 18h6l-12 20h8l-14 22h44l-14-22h8l-12-20h6z"
def pines(items):
    return ''.join(f'<use href="#pine" transform="translate({x} {y}) scale({k})"/>' for x, y, k in items)
def ly(inner, k=None, cls='', extra=''):
    """one layer of a scene: its own <svg>, so parallax and the train are moved by the compositor without repainting"""
    dk = f' data-k="{k}"' if k is not None else ''
    return f'<svg class="ly{cls}"{dk}{extra} viewBox="0 0 1600 520" preserveAspectRatio="xMidYMax slice" aria-hidden="true">{inner}</svg>\n        '

DEFS = f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <defs>
    <radialGradient id="halo"><stop offset=".25" stop-color="var(--lit)" stop-opacity=".6"/><stop offset="1" stop-color="var(--lit)" stop-opacity="0"/></radialGradient>
    <linearGradient id="beam"><stop offset="0" stop-color="var(--lit)" stop-opacity=".55"/><stop offset="1" stop-color="var(--lit)" stop-opacity="0"/></linearGradient>
    <linearGradient id="gPeaks" x1="0" y1="0" x2="0" y2="1"><stop offset="0" style="stop-color:color-mix(in oklab,var(--far) 62%,var(--sky))"/><stop offset=".6" style="stop-color:color-mix(in oklab,var(--far) 30%,var(--sky))"/></linearGradient>
    <linearGradient id="gFar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--far)"/><stop offset=".55" style="stop-color:color-mix(in oklab,var(--far) 60%,var(--sky))"/></linearGradient>
    <linearGradient id="gMid" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--mid)"/><stop offset=".7" style="stop-color:color-mix(in oklab,var(--mid) 70%,var(--far))"/></linearGradient>
    <linearGradient id="gMist" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--sky)" stop-opacity="0"/><stop offset=".55" stop-color="var(--sky)" stop-opacity=".5"/><stop offset="1" stop-color="var(--sky)" stop-opacity="0"/></linearGradient>
    <linearGradient id="gStone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--struct)"/><stop offset="1" style="stop-color:color-mix(in oklab,var(--struct) 55%,var(--near))"/></linearGradient>
    <radialGradient id="puffG"><stop offset=".15" stop-color="var(--on)"/><stop offset="1" stop-color="var(--on)" stop-opacity="0"/></radialGradient>
    <radialGradient id="haloA"><stop offset=".1" stop-color="var(--accent)" stop-opacity=".85"/><stop offset="1" stop-color="var(--accent)" stop-opacity="0"/></radialGradient>
    <linearGradient id="shadG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset=".45" stop-color="#000" stop-opacity=".34"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>
    <linearGradient id="glowG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--accent)" stop-opacity="0"/><stop offset=".5" stop-color="var(--accent)" stop-opacity=".75"/><stop offset="1" stop-color="var(--accent)" stop-opacity="0"/></linearGradient>
    <linearGradient id="pulseG"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <clipPath id="strip"><path d="M-426 273h602c28 0 50 4 68 10h-670z"/></clipPath>
    <pattern id="speck" width="80" height="50" patternUnits="userSpaceOnUse"><rect x="35.7" y="27.4" width="1.7" height="1" fill="var(--on)" opacity="0.19"/><rect x="14.6" y="25.1" width="1" height="0.8" fill="var(--on)" opacity="0.12"/><rect x="42.6" y="43.6" width="0.8" height="1.3" fill="#000" opacity="0.33"/><rect x="51.7" y="30.2" width="1" height="1.3" fill="var(--on)" opacity="0.18"/><rect x="4.7" y="9.3" width="1" height="1.3" fill="var(--on)" opacity="0.17"/><rect x="34.8" y="41.3" width="1" height="1.3" fill="var(--on)" opacity="0.10"/><rect x="6.7" y="32.1" width="1.7" height="1.3" fill="#000" opacity="0.31"/><rect x="55.9" y="15.4" width="1" height="1.3" fill="var(--on)" opacity="0.11"/><rect x="60.5" y="19.6" width="1.3" height="1" fill="var(--on)" opacity="0.10"/><rect x="54.1" y="10.5" width="0.8" height="1" fill="var(--on)" opacity="0.21"/><rect x="33.2" y="27.7" width="1" height="1.3" fill="var(--on)" opacity="0.11"/><rect x="26.3" y="47.2" width="0.8" height="0.8" fill="var(--on)" opacity="0.12"/><rect x="4.7" y="39.1" width="1" height="1.3" fill="#000" opacity="0.24"/><rect x="15.1" y="35.9" width="1" height="1" fill="#000" opacity="0.18"/><rect x="33.2" y="10.4" width="1.3" height="1.3" fill="var(--on)" opacity="0.24"/><rect x="16.6" y="19.3" width="0.8" height="0.8" fill="#000" opacity="0.20"/><rect x="20.4" y="37.9" width="1.3" height="1" fill="var(--on)" opacity="0.11"/><rect x="16.5" y="31.2" width="0.8" height="1.3" fill="var(--on)" opacity="0.20"/><rect x="10.1" y="28.8" width="1" height="1" fill="var(--on)" opacity="0.12"/><rect x="71.8" y="40.1" width="1" height="1.3" fill="var(--on)" opacity="0.22"/><rect x="74.3" y="9.6" width="1.7" height="1" fill="#000" opacity="0.24"/><rect x="8.2" y="1.9" width="1.3" height="0.8" fill="#000" opacity="0.23"/><rect x="33.2" y="44.3" width="1.7" height="1" fill="var(--on)" opacity="0.25"/><rect x="77.2" y="6.2" width="1.7" height="1.3" fill="#000" opacity="0.27"/><rect x="5.9" y="10.4" width="1" height="1.3" fill="var(--on)" opacity="0.14"/><rect x="35.2" y="3.0" width="1" height="1" fill="var(--on)" opacity="0.19"/><rect x="10.4" y="17.7" width="1.7" height="1" fill="#000" opacity="0.28"/><rect x="46.2" y="6.9" width="0.8" height="0.8" fill="var(--on)" opacity="0.16"/><rect x="24.6" y="1.6" width="0.8" height="1" fill="var(--on)" opacity="0.15"/><rect x="10.8" y="3.5" width="1.7" height="1.3" fill="var(--on)" opacity="0.11"/><rect x="74.0" y="36.1" width="1" height="1" fill="var(--on)" opacity="0.21"/><rect x="71.2" y="42.7" width="1.7" height="0.8" fill="#000" opacity="0.26"/><rect x="49.4" y="18.7" width="0.8" height="1.3" fill="var(--on)" opacity="0.11"/><rect x="9.1" y="12.6" width="1.7" height="1.3" fill="var(--on)" opacity="0.25"/><rect x="54.8" y="22.4" width="1.7" height="1.3" fill="var(--on)" opacity="0.22"/><rect x="2.4" y="29.5" width="1.7" height="0.8" fill="var(--on)" opacity="0.21"/><rect x="39.3" y="30.1" width="1.7" height="1" fill="#000" opacity="0.23"/><rect x="11.3" y="30.0" width="1" height="1" fill="#000" opacity="0.24"/><rect x="70.4" y="16.0" width="1.3" height="0.8" fill="#000" opacity="0.30"/><rect x="59.6" y="9.8" width="1" height="1" fill="var(--on)" opacity="0.25"/><rect x="16.6" y="6.6" width="1.3" height="0.8" fill="#000" opacity="0.33"/><rect x="21.9" y="8.3" width="1.7" height="1" fill="var(--on)" opacity="0.13"/><rect x="32.7" y="30.7" width="1.7" height="1.3" fill="var(--on)" opacity="0.23"/><rect x="77.6" y="22.2" width="0.8" height="0.8" fill="var(--on)" opacity="0.20"/><rect x="53.6" y="13.8" width="1.3" height="1" fill="#000" opacity="0.26"/><rect x="50.6" y="19.9" width="1" height="0.8" fill="#000" opacity="0.21"/><rect x="61.6" y="39.0" width="0.8" height="1" fill="var(--on)" opacity="0.19"/><rect x="50.6" y="18.1" width="0.8" height="1.3" fill="var(--on)" opacity="0.23"/><rect x="20.2" y="35.0" width="1.7" height="1.3" fill="#000" opacity="0.19"/><rect x="21.5" y="16.9" width="1" height="1" fill="#000" opacity="0.29"/><rect x="17.7" y="20.1" width="1.7" height="0.8" fill="var(--on)" opacity="0.13"/><rect x="70.1" y="0.3" width="1.3" height="1" fill="var(--on)" opacity="0.26"/><rect x="7.8" y="42.4" width="0.8" height="0.8" fill="var(--on)" opacity="0.16"/><rect x="6.9" y="15.2" width="1.3" height="1" fill="#000" opacity="0.31"/><rect x="27.5" y="4.1" width="1.7" height="1" fill="#000" opacity="0.30"/><rect x="38.5" y="1.4" width="0.8" height="1" fill="#000" opacity="0.19"/><rect x="26.5" y="38.6" width="1" height="1" fill="var(--on)" opacity="0.18"/><rect x="57.2" y="41.2" width="1.7" height="1" fill="#000" opacity="0.28"/><rect x="59.9" y="21.5" width="1.3" height="1.3" fill="#000" opacity="0.19"/><rect x="40.6" y="44.5" width="1.3" height="1" fill="#000" opacity="0.33"/><rect x="68.7" y="29.9" width="1.3" height="0.8" fill="#000" opacity="0.25"/><rect x="45.3" y="9.8" width="0.8" height="1.3" fill="var(--on)" opacity="0.16"/><rect x="42.5" y="2.2" width="1.7" height="1.3" fill="#000" opacity="0.26"/><rect x="38.8" y="33.9" width="0.8" height="1.3" fill="var(--on)" opacity="0.25"/><rect x="63.2" y="19.8" width="1" height="1" fill="var(--on)" opacity="0.15"/><rect x="71.2" y="45.8" width="1.7" height="1.3" fill="var(--on)" opacity="0.13"/><rect x="48.8" y="45.3" width="1" height="1.3" fill="#000" opacity="0.16"/><rect x="15.3" y="11.1" width="1.3" height="1" fill="#000" opacity="0.20"/><rect x="39.4" y="24.5" width="0.8" height="1.3" fill="#000" opacity="0.29"/><rect x="55.4" y="43.1" width="0.8" height="1" fill="#000" opacity="0.31"/><rect x="48.6" y="26.4" width="1" height="1.3" fill="var(--on)" opacity="0.19"/><rect x="46.3" y="6.7" width="1.3" height="0.8" fill="var(--on)" opacity="0.15"/><rect x="72.9" y="10.7" width="1" height="0.8" fill="var(--on)" opacity="0.14"/><rect x="57.4" y="12.7" width="0.8" height="1" fill="#000" opacity="0.24"/><rect x="62.4" y="6.2" width="1.7" height="1.3" fill="#000" opacity="0.16"/><rect x="15.9" y="33.4" width="1.3" height="0.8" fill="#000" opacity="0.27"/><rect x="27.1" y="48.9" width="1" height="0.8" fill="var(--on)" opacity="0.10"/><rect x="60.2" y="30.1" width="1.7" height="0.8" fill="var(--on)" opacity="0.12"/><rect x="13.6" y="7.7" width="1.3" height="1.3" fill="var(--on)" opacity="0.11"/><rect x="75.2" y="22.6" width="0.8" height="1" fill="var(--on)" opacity="0.17"/><rect x="28.0" y="10.3" width="1.3" height="0.8" fill="#000" opacity="0.17"/><rect x="15.8" y="20.0" width="1.3" height="1.3" fill="var(--on)" opacity="0.25"/><rect x="47.8" y="4.6" width="0.8" height="1" fill="#000" opacity="0.30"/><rect x="55.7" y="42.2" width="1.7" height="1.3" fill="#000" opacity="0.25"/><rect x="77.6" y="39.4" width="1.3" height="1" fill="#000" opacity="0.29"/><rect x="61.5" y="39.9" width="1.7" height="0.8" fill="#000" opacity="0.32"/><rect x="54.9" y="37.6" width="1" height="1" fill="var(--on)" opacity="0.13"/><rect x="63.0" y="14.8" width="0.8" height="0.8" fill="#000" opacity="0.34"/><rect x="71.3" y="2.4" width="1.3" height="1.3" fill="var(--on)" opacity="0.13"/><rect x="32.1" y="8.9" width="0.8" height="1" fill="var(--on)" opacity="0.18"/><rect x="16.8" y="5.9" width="1.7" height="1.3" fill="var(--on)" opacity="0.20"/><rect x="58.4" y="12.6" width="1.7" height="1.3" fill="var(--on)" opacity="0.13"/><rect x="29.7" y="4.8" width="1.3" height="1" fill="#000" opacity="0.26"/><rect x="40.1" y="47.4" width="0.8" height="1.3" fill="var(--on)" opacity="0.20"/><rect x="43.4" y="32.8" width="0.8" height="1" fill="#000" opacity="0.19"/><rect x="37.3" y="8.3" width="1.7" height="1.3" fill="#000" opacity="0.17"/><rect x="74.7" y="20.6" width="1.7" height="1.3" fill="var(--on)" opacity="0.18"/><rect x="38.2" y="13.2" width="1.3" height="1.3" fill="#000" opacity="0.21"/><rect x="1.1" y="12.0" width="0.8" height="1.3" fill="var(--on)" opacity="0.22"/><rect x="30.8" y="44.0" width="1.7" height="0.8" fill="#000" opacity="0.29"/><rect x="25.2" y="39.1" width="1" height="1" fill="#000" opacity="0.21"/><rect x="59.7" y="2.2" width="0.8" height="1.3" fill="#000" opacity="0.19"/><rect x="75.8" y="12.0" width="0.8" height="0.8" fill="#000" opacity="0.24"/><rect x="16.1" y="2.6" width="1" height="0.8" fill="var(--on)" opacity="0.12"/><rect x="32.9" y="29.5" width="1.7" height="1" fill="#000" opacity="0.26"/><rect x="78.8" y="46.7" width="1" height="0.8" fill="var(--on)" opacity="0.18"/><rect x="24.4" y="24.9" width="1.3" height="1" fill="var(--on)" opacity="0.21"/><rect x="44.6" y="29.0" width="1.3" height="0.8" fill="var(--on)" opacity="0.14"/><rect x="77.4" y="44.9" width="0.8" height="1.3" fill="var(--on)" opacity="0.14"/><rect x="33.6" y="30.5" width="0.8" height="0.8" fill="var(--on)" opacity="0.11"/><rect x="6.8" y="33.1" width="1" height="1.3" fill="#000" opacity="0.25"/><rect x="28.0" y="16.6" width="1.7" height="1.3" fill="var(--on)" opacity="0.24"/><rect x="63.4" y="21.9" width="1" height="1" fill="var(--on)" opacity="0.14"/><rect x="64.0" y="18.1" width="1.3" height="1" fill="var(--on)" opacity="0.22"/><rect x="72.7" y="21.0" width="1.3" height="1.3" fill="var(--on)" opacity="0.24"/><rect x="6.2" y="4.1" width="1.7" height="1.3" fill="var(--on)" opacity="0.23"/><rect x="0.7" y="15.2" width="0.8" height="1.3" fill="var(--on)" opacity="0.22"/><rect x="54.8" y="13.9" width="1" height="0.8" fill="var(--on)" opacity="0.22"/><rect x="28.9" y="5.8" width="1.7" height="1.3" fill="#000" opacity="0.32"/><rect x="54.3" y="13.7" width="1.3" height="1" fill="var(--on)" opacity="0.16"/><rect x="73.8" y="43.8" width="1" height="0.8" fill="var(--on)" opacity="0.16"/><rect x="28.7" y="19.4" width="1.7" height="0.8" fill="#000" opacity="0.23"/><rect x="30.8" y="7.6" width="1" height="0.8" fill="var(--on)" opacity="0.17"/><rect x="67.5" y="39.8" width="1" height="1.3" fill="var(--on)" opacity="0.13"/><rect x="23.4" y="1.1" width="1.7" height="0.8" fill="#000" opacity="0.21"/><rect x="43.1" y="16.4" width="1.3" height="1.3" fill="var(--on)" opacity="0.15"/><rect x="2.1" y="32.0" width="0.8" height="1.3" fill="#000" opacity="0.24"/><rect x="56.3" y="24.0" width="1.3" height="1" fill="var(--on)" opacity="0.15"/><rect x="76.5" y="32.9" width="1.7" height="1" fill="var(--on)" opacity="0.22"/><rect x="55.9" y="44.8" width="1.7" height="1.3" fill="var(--on)" opacity="0.10"/><rect x="29.9" y="4.4" width="1.7" height="1.3" fill="#000" opacity="0.25"/><rect x="56.1" y="39.3" width="1.7" height="1" fill="#000" opacity="0.20"/><rect x="12.8" y="31.1" width="1" height="1" fill="var(--on)" opacity="0.17"/><rect x="23.1" y="47.5" width="0.8" height="1" fill="var(--on)" opacity="0.12"/><rect x="51.2" y="38.0" width="1" height="0.8" fill="#000" opacity="0.16"/><rect x="38.0" y="39.2" width="1.3" height="0.8" fill="var(--on)" opacity="0.16"/><rect x="46.5" y="29.4" width="1.7" height="1.3" fill="var(--on)" opacity="0.17"/><rect x="70.7" y="19.7" width="1.3" height="1.3" fill="var(--on)" opacity="0.23"/><rect x="37.9" y="12.8" width="1.7" height="1" fill="#000" opacity="0.30"/><rect x="7.3" y="42.3" width="1.7" height="0.8" fill="var(--on)" opacity="0.12"/><rect x="63.1" y="47.8" width="1.3" height="0.8" fill="#000" opacity="0.20"/><rect x="0.9" y="23.2" width="1.3" height="1" fill="#000" opacity="0.29"/><rect x="47.9" y="7.7" width="1" height="1" fill="var(--on)" opacity="0.25"/><rect x="64.0" y="6.4" width="1.3" height="1.3" fill="var(--on)" opacity="0.12"/><rect x="60.9" y="0.1" width="1" height="0.8" fill="var(--on)" opacity="0.14"/><rect x="56.6" y="4.8" width="1.7" height="1.3" fill="var(--on)" opacity="0.25"/><rect x="46.3" y="42.0" width="1.3" height="0.8" fill="#000" opacity="0.24"/><rect x="72.4" y="4.5" width="1.7" height="0.8" fill="var(--on)" opacity="0.17"/><rect x="39.0" y="46.4" width="1.3" height="1" fill="var(--on)" opacity="0.11"/><rect x="24.2" y="22.9" width="0.8" height="1" fill="var(--on)" opacity="0.12"/></pattern>
    <linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".3"/><stop offset=".3" stop-color="#fff" stop-opacity=".04"/><stop offset=".62" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".45"/></linearGradient>
    <pattern id="bay" x="0" y="314" width="130" height="220" patternUnits="userSpaceOnUse">
      <path d="M0 0H130V220H112V66A47 47 0 0 0 18 66V220H0Z" fill="url(#gStone)"/>
      <path d="M112 66A47 47 0 0 0 18 66" fill="none" stroke="var(--lit)" stroke-opacity=".16" stroke-width="3"/>
      <rect x="112" y="66" width="5" height="154" fill="var(--lit)" opacity=".1"/>
      <rect x="0" y="66" width="18" height="154" fill="var(--near)" opacity=".18"/>
    </pattern>
    <pattern id="win" width="11" height="15" patternUnits="userSpaceOnUse"><rect x="3" y="4" width="5" height="7" fill="var(--lit)"/></pattern>
    <pattern id="wire" x="0" y="220.6" width="130" height="79.4" patternUnits="userSpaceOnUse"><path d="M0 0H130V1.6H67V8H72V10H67V80H63V10H58V8H63V1.6H0Z" fill="var(--struct)"/></pattern>
    <path id="pine" d="{PINE}"/>

    <symbol id="peaks" viewBox="0 0 1600 520" preserveAspectRatio="none" overflow="visible">
      <path d="M0 215L140 150 250 190 400 110 560 185 700 140 860 200 1010 150 1160 205 1330 130 1480 180 1600 150V700H0Z" fill="url(#gPeaks)"/>
      <path d="M400 110L560 185 470 232ZM1330 130L1480 180 1400 236ZM700 140L860 200 760 236ZM1010 150L1160 205 1070 240Z" fill="var(--lit)" opacity=".12"/>
    </symbol>
    <symbol id="far" viewBox="0 0 1600 520" preserveAspectRatio="none" overflow="visible">
      <path d="M0 250C150 190 300 215 460 240S760 170 940 215 1300 180 1600 230V700H0Z" fill="url(#gFar)"/>
      <path d="M0 250C150 190 300 215 460 240S760 170 940 215 1300 180 1600 230" fill="none" stroke="var(--lit)" stroke-opacity=".3" stroke-width="2"/>
      <rect y="232" width="1600" height="110" fill="url(#gMist)"/>
    </symbol>
    <symbol id="mid" viewBox="0 0 1600 520" preserveAspectRatio="none" overflow="visible">
      <path d="M0 330C200 280 380 345 600 335S980 290 1180 340 1480 300 1600 325V620H0Z" fill="url(#gMid)"/>
      <path d="M600 335L790 312 700 430ZM1180 340L1330 316 1270 430Z" fill="var(--lit)" opacity=".07"/>
      <path d="M180 302L340 326 250 430ZM900 303L1060 318 980 430Z" fill="var(--near)" opacity=".1"/>
      <path d="M0 330C200 280 380 345 600 335S980 290 1180 340 1480 300 1600 325" fill="none" stroke="var(--lit)" stroke-opacity=".22" stroke-width="2"/>
      <path d="M0 392C300 376 520 386 800 380S1300 368 1600 378V620H0Z" style="fill:color-mix(in oklab,var(--lit) var(--haze),var(--sky))"/>
      <rect y="350" width="1600" height="80" fill="url(#gMist)" opacity=".7"/>
    </symbol>
    <symbol id="viaduct" viewBox="0 0 1600 520" preserveAspectRatio="none" overflow="visible">
      <rect y="314" width="1600" height="220" fill="url(#bay)"/>
      <rect y="296" width="1600" height="18" fill="var(--struct)"/>
      <rect y="296" width="1600" height="2" fill="var(--lit)" opacity=".3"/>
      <rect y="311" width="1600" height="3" fill="var(--near)" opacity=".35"/>
    </symbol>
    <symbol id="foreA" viewBox="0 0 1600 520" preserveAspectRatio="none" overflow="visible">
      <g style="fill:color-mix(in oklab,var(--near) 68%,var(--struct))">
        <path d="M0 420C160 396 300 430 520 418S900 380 1120 408 1440 388 1600 404V620H0Z"/>
        {pines([(70,350,1),(104,364,.75),(430,362,1),(462,374,.7),(770,338,1),(806,352,.8),(842,344,1),(1330,340,1),(1366,354,.75),(1540,346,1)])}
        <path d="M248 392v30h4v-30zM978 376v30h4v-30zM1198 380v30h4v-30z"/><circle cx="250" cy="386" r="17"/><circle cx="980" cy="370" r="17"/><circle cx="1004" cy="380" r="12"/><circle cx="1200" cy="374" r="16"/>
      </g>
    </symbol>
    <symbol id="foreB" viewBox="0 0 1600 520" preserveAspectRatio="none" overflow="visible">
      <g fill="var(--near)">
        <path d="M0 448C180 418 420 462 700 452S1150 414 1600 446V526H0Z"/>
        {pines([(190,360,1.25),(236,386,.9),(600,392,.95),(1150,346,1.3),(1200,374,1),(1480,372,1.1)])}
      </g>
    </symbol>
  </defs>
</svg>'''

def wrap(label, back, rail, front='', dur=22):
    return (f'<div class="scene" role="img" aria-label="{label}">\n        ' + back + ly(rail, cls=' train', extra=f' data-dur="{dur}"')
            + ly('<use href="#foreA"/>', -34) + ly('<use href="#foreB"/>' + front) + '</div>')

def back(sky, far_extra, town, mid_extra, tail=''):
    return (ly(sky, 130) + ly('<use href="#peaks"/>', 96) + ly('<use href="#far"/>' + far_extra, 62)
            + ly(town + '<use href="#mid"/>' + mid_extra, 24) + ly('<use href="#viaduct"/>' + tail))

# ---- small moving parts -------------------------------------------------
def wheel(cx, cy, r, dur, drive=False):
    if drive:
        inner = ('<circle r="13" fill="var(--train)"/><circle r="8.5" fill="none" stroke="var(--accent)" stroke-width="2.5"/>'
                 '<path d="M-8 0H8M0-8V8M-5.7-5.7L5.7 5.7M-5.7 5.7L5.7-5.7" stroke="var(--accent)" stroke-width="1.4"/>'
                 '<circle r="2.6" fill="var(--accent)"/><circle cx="5" r="2.2" fill="var(--on)"/>')
    else:
        k = r - 1.6
        inner = (f'<circle r="{r}" fill="var(--train)"/><circle r="{k:.1f}" fill="none" stroke="var(--far)" stroke-width="1.1"/>'
                 f'<path d="M-{k:.1f} 0H{k:.1f}M0-{k:.1f}V{k:.1f}" stroke="var(--far)" stroke-width="1.2"/>')
    return f'<g transform="translate({cx} {cy})"><g class="rot" style="animation-duration:{dur}s">{inner}</g></g>'

def lamp(shape, lo=.12):
    d = random.uniform(5, 15); t = random.uniform(0, d)
    return shape.replace('/>', f' class="lamp" style="--d:{d:.1f}s;--t:-{t:.1f}s;--b:{lo}"/>', 1)

def togglers(areas, per, ymax=300):
    out = []
    for (x, y, w, h) in areas:
        cells = [(11*i+3, 15*j+4) for i in range(0, 160) for j in range(0, 40)
                 if 11*i+3 >= x and 11*i+8 <= x+w and 15*j+4 >= y and 15*j+11 <= min(y+h, ymax)]
        for (cx, cy) in random.sample(cells, min(per, len(cells))):
            d = random.uniform(6, 18); t = random.uniform(0, d)
            out.append(f'<rect x="{cx-.5}" y="{cy-.5}" width="6" height="8" class="lamp off" style="--d:{d:.1f}s;--t:-{t:.1f}s"/>')
    return '<g class="bld">' + ''.join(out) + '</g>'

def puffs(cx, cy, r, n, cls, dur):
    return ''.join(f'<circle class="{cls}" cx="{cx}" cy="{cy}" r="{r}" style="animation-delay:-{i*dur/n:.2f}s"/>' for i in range(n))

def skin(cid, shapes, x, y, w, h):
    """clip of the body shapes + the overlays that give it grain, a lit top and a shaded belly"""
    return (f'<clipPath id="{cid}">{shapes}</clipPath><g clip-path="url(#{cid})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#shade)"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#speck)"/></g>')
def shadow(x, w):
    return f'<rect x="{x}" y="294" width="{w}" height="11" fill="url(#shadG)"/>'

# ---- 1930: steam ---------------------------------------------------------
def car30(x):
    body = (f'<rect x="{x}" y="264" width="88" height="28" rx="3"/><rect x="{x-2}" y="259" width="92" height="6" rx="3"/><rect x="{x+14}" y="255" width="60" height="5" rx="2"/>'
            f'<rect x="{x+24}" y="252" width="6" height="4" rx="1"/><rect x="{x+58}" y="252" width="6" height="4" rx="1"/>'
            f'<rect x="{x+6}" y="292" width="76" height="3"/><rect x="{x+88}" y="285" width="6" height="3"/>')
    lit = ''.join(f'<rect x="{x+13+i*13}" y="270" width="8" height="10" rx="1"/>' for i in range(5))
    trim = (f'<rect x="{x}" y="283.5" width="88" height="2"/>'
            f'<rect x="{x+4}" y="267" width="1.5" height="23"/><rect x="{x+82.5}" y="267" width="1.5" height="23"/>')
    wheels = ''.join(wheel(x+c, 296, 5, .54) for c in (13, 25, 63, 75))
    return body, lit, trim, wheels
c30 = [car30(x) for x in (-290, -196, -102)]
B30 = f'''{''.join(c[0] for c in c30)}            <path d="M-6 268h50v24h-50zM-2 268q22-13 42 0zM44 286h8v3h-8z"/>            <rect x="50" y="250" width="34" height="42"/><rect x="46" y="246" width="42" height="5" rx="2"/>            <rect x="84" y="262" width="128" height="24" rx="10"/><rect x="204" y="260" width="22" height="28" rx="4"/>            <path d="M210 260v-16h-3v-5h18v5h-3v16zM150 263a10 10 0 0 1 20 0zM112 263a7 7 0 0 1 14 0zM176 254h3v9h-3zM174 252h7v3h-7zM226 252h6v8h-6z"/>            <rect x="84" y="286" width="150" height="4"/><path d="M234 286l20 14h-20z"/>'''
STEAM = f'''<g>
          {shadow(-296, 548)}
          <g fill="url(#puffG)">{puffs(216, 234, 30, 9, 'puff', 4.4)}{puffs(226, 293, 12, 3, 'puff2', 1.5)}</g>
          <path d="M234 250L470 226V296L234 262Z" fill="url(#beam)" opacity=".5"/>
          <g fill="var(--train)">{B30}</g>{skin('cS', B30, -300, 238, 566, 62)}
          <g fill="var(--struct)"><rect x="120" y="262" width="2" height="24"/><rect x="178" y="262" width="2" height="24"/><rect x="196" y="262" width="2" height="24"/><rect x="-6" y="277" width="50" height="1.5"/><rect x="50" y="272" width="34" height="1.5"/></g>
          <path d="M92 271H204" stroke="var(--far)" stroke-width="1.2" fill="none"/>
          <rect x="94" y="265" width="106" height="3" rx="1.5" fill="var(--lit)" opacity=".28"/>
          <g fill="var(--accent)">{''.join(c[2] for c in c30)}<rect x="228" y="281" width="6" height="12"/><rect x="-6" y="283.5" width="50" height="2"/></g>
          {''.join(c[3] for c in c30)}{wheel(6, 295, 6, .65)}{wheel(22, 295, 6, .65)}{wheel(38, 295, 6, .65)}
          {wheel(68, 293, 7, .76)}{wheel(198, 293, 7, .76)}{wheel(218, 293, 7, .76)}
          {wheel(108, 287, 13, 1.41, True)}{wheel(138, 287, 13, 1.41, True)}{wheel(168, 287, 13, 1.41, True)}
          <rect class="pist" x="172" y="286" width="42" height="2" fill="var(--on)"/>
          <rect class="rod" x="104" y="285.5" width="68" height="3" rx="1.5" fill="var(--on)"/>
          <rect x="206" y="282" width="22" height="11" rx="2" fill="var(--train)"/><rect x="206" y="284" width="22" height="1.5" fill="var(--struct)"/>
          <g fill="var(--lit)">{''.join(c[1] for c in c30)}<rect x="56" y="256" width="20" height="13" rx="1"/><circle cx="229" cy="256" r="4"/></g>
          <circle cx="67" cy="261.5" r="3.2" fill="var(--train)"/><path d="M61 269a6 4.6 0 0 1 12 0z" fill="var(--train)"/>
          <rect class="lamp" style="--d:.9s;--b:.45" x="55" y="287" width="22" height="4" rx="2" fill="var(--accent)"/>
          <circle cx="-291" cy="288" r="2.4" fill="var(--accent)"/>
        </g>'''

# ---- 2000: electric ------------------------------------------------------
def car00(x, front=False):
    body = (f'<rect x="{x}" y="260" width="110" height="33" rx="5"/><rect x="{x+10}" y="255.5" width="30" height="5" rx="2"/><rect x="{x+66}" y="255.5" width="34" height="5" rx="2"/>'
            f'<rect x="{x+42}" y="293" width="26" height="5" rx="1"/><rect x="{x+9}" y="293" width="28" height="3.5" rx="1"/><rect x="{x+73}" y="293" width="28" height="3.5" rx="1"/>')
    lit = ''.join(f'<rect x="{x+c}" y="267" width="14" height="11" rx="2"/>' for c in (8, 26, 68, 86)) + f'<rect x="{x+49}" y="267" width="4.5" height="14" rx="1.5"/><rect x="{x+55.5}" y="267" width="4.5" height="14" rx="1.5"/>'
    trim = f'<rect x="{x}" y="283" width="110" height="3"/>'
    door = f'<rect x="{x+46.5}" y="264.5" width="16" height="27" rx="2"/><path d="M{x+54.5} 264.5v27"/>'
    bellows = f'<rect x="{x+110}" y="263" width="4" height="29"/>'
    wheels = ''.join(wheel(x+c, 296, 5, .4) for c in (16, 30, 80, 94))
    return body, lit, trim, door, bellows, wheels
c00 = [car00(x) for x in (-342, -228, -114)]
B00 = f'''{''.join(c[0] for c in c00)}            <path d="M0 260h84c22 0 36 12 44 33H0zM9 293h28v3.5H9zM74 293h30v3.5H74zM42 293h26v5H42zM10 255.5h40v5H10z"/>            <path d="M-190 255h30v3h-30zM-176 248h3v8h-3zM-150 248h3v8h-3z"/>'''
EMU = f'''<g>
          {shadow(-344, 470)}
          <path d="M126 276L400 262V298L126 290Z" fill="url(#beam)" opacity=".45"/>
          <g fill="var(--struct)">{''.join(c[4] for c in c00)}</g>
          <g fill="var(--train)">{B00}</g>{skin('cE', B00, -346, 250, 476, 50)}
          <g fill="none" stroke="var(--train)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"><path d="M-182 255l20-8-16-8M-190 239.5h26"/></g>
          <g fill="var(--lit)">{''.join(c[1] for c in c00)}<rect x="8" y="267" width="14" height="11" rx="2"/><rect x="26" y="267" width="14" height="11" rx="2"/><rect x="49" y="267" width="4.5" height="14" rx="1.5"/><rect x="55.5" y="267" width="4.5" height="14" rx="1.5"/><path d="M70 266h16c12 1 20 6 25 13H70z"/><circle cx="121" cy="286" r="2.6"/></g>
          <g fill="var(--accent)">{''.join(c[2] for c in c00)}<path d="M0 283h121l3 3H0z"/><circle cx="-340" cy="289" r="2"/></g>
          <rect x="-342" y="288" width="466" height="1" fill="var(--lit)" opacity=".45"/>
          <g fill="none" stroke="var(--far)" stroke-width=".9" opacity=".8">{''.join(c[3] for c in c00)}<rect x="46.5" y="264.5" width="16" height="27" rx="2"/><path d="M54.5 264.5v27"/></g>
          {''.join(c[5] for c in c00)}{wheel(18, 296, 5, .4)}{wheel(32, 296, 5, .4)}{wheel(84, 296, 5, .4)}{wheel(98, 296, 5, .4)}
        </g>'''

# ---- 2040: maglev --------------------------------------------------------
MAGLEV = ('''<g>
          <rect class="lamp" style="--d:2.4s;--b:.45" x="-446" y="289" width="730" height="18" fill="url(#glowG)"/>
          <path d="M270 280L620 262V300L270 292Z" fill="url(#beam)" opacity=".6"/>
          <path d="M-432 264c-6 0-10 6-10 14v16h720c-16-16-50-30-108-30zM-420 264l-14-12h26l12 12zM-60 264h40l-4-5h-32z"/><clipPath id="cM"><path d="M-432 264c-6 0-10 6-10 14v16h720c-16-16-50-30-108-30zM-420 264l-14-12h26l12 12zM-60 264h40l-4-5h-32z"/></clipPath><g clip-path="url(#cM)"><rect x="-446" y="250" width="730" height="46" fill="url(#shade)"/><rect x="-446" y="250" width="730" height="46" fill="url(#speck)"/></g>
          <path d="M-426 273h602c28 0 50 4 68 10h-670z" fill="var(--lit)"/>
          <g clip-path="url(#strip)"><rect class="pulse" x="-540" y="270" width="110" height="16" fill="url(#pulseG)"/></g>
          <g fill="var(--train)">''' + ''.join(f'<rect x="{x}" y="273" width="3" height="10"/>' for x in range(-400, 180, 38)) + '''</g>
          <g fill="none" stroke="var(--far)" stroke-width=".9"><rect x="-364" y="267" width="20" height="24" rx="3"/><rect x="-174" y="267" width="20" height="24" rx="3"/><rect x="16" y="267" width="20" height="24" rx="3"/><path d="M-270 264v30M-80 264v30M110 264v30"/></g>
          <path d="M150 264c44 0 74 6 96 16-30-6-62-9-96-9z" fill="var(--accent)" opacity=".75"/>
          <rect x="-442" y="289" width="716" height="2" fill="var(--accent)"/>
          <g fill="var(--lit)">''' + ''.join(f'<circle cx="{x}" cy="293.5" r="1.3" class="lamp" style="--d:1.6s;--t:-{i*.1:.1f}s;--b:.1"/>' for i, x in enumerate(range(-420, 250, 42))) + '''</g>
          <circle cx="-440" cy="282" r="2.2" fill="var(--accent)"/>
        </g>''').replace('<path d="M-432 264c', '<path fill="var(--train)" d="M-432 264c')

def big(t):
    i = t.index('>') + 1
    return t[:i] + '<g transform="translate(0 300) scale(1.3) translate(0 -300)">' + t[i:] + '</g>'
STEAM, EMU, MAGLEV = big(STEAM), big(EMU), big(MAGLEV)

# ---- the three scenes ----------------------------------------------------
w30 = [(250,278,6,8),(261,278,6,8),(280,282,6,8),(291,282,6,8),(310,278,6,8),(321,278,6,8),(342,258,6,9),(356,258,6,9),(370,258,6,9),(342,276,6,9),(356,276,6,9),(370,276,6,9),(462,282,7,8),(477,282,7,8),(492,282,7,8),(462,298,7,8),(492,298,7,8),(588,282,6,8),(600,282,6,8),(266,264,5,7),(306,254,5,7),(398,250,5,7),(478,262,5,7),(606,262,5,7)]
win30 = ''.join((lamp if i % 2 else (lambda q: q))(f'<rect x="{x}" y="{y}" width="{w}" height="{h}"/>') for i, (x, y, w, h) in enumerate(w30))
S1930 = wrap("A steam train crossing a stone viaduct at dawn, a small factory town on the hill behind it",
 back('''<circle cx="1180" cy="212" r="270" fill="url(#halo)"/><circle cx="1180" cy="212" r="74" fill="var(--lit)"/>
        <g class="drift" fill="none" stroke="var(--ink)" stroke-width="2" stroke-linecap="round" opacity=".55"><path d="M900 118q8-8 16 0q8-8 16 0"/><path d="M948 96q6-6 12 0q6-6 12 0"/><path d="M866 88q5-5 10 0q5-5 10 0"/></g>''',
  '',
  f'''<g fill="url(#puffG)">{puffs(551, 204, 20, 5, 'puff3', 10)}{puffs(592, 218, 16, 4, 'puff3', 8)}</g>
        <path class="bld2" d="M256 252h34v110h-34zM298 240h40v122h-40zM388 236h34v126h-34zM466 250h44v112h-44zM520 262h56v100h-56zM596 250h46v112h-46z"/>
        <g class="bld">
          <path d="M244 268l15-12 15 12v94h-30zM274 272l15-12 15 12v90h-30zM304 266l15-12 15 12v96h-30zM252 250h5v14h-5zM312 248h5v14h-5z"/>
          <path d="M334 246h50v116h-50zM351 214h16v32h-16zM348 214l11-17 11 17z"/>
          <path d="M384 262l24-16 24 16v100h-48zM432 250h20v112h-20zM430 250l12-50 12 50z"/>
          <path d="M452 270h60v92h-60zM512 284l17-12v12l17-12v12l17-12v12l17-12v90h-68zM580 268h36v94h-36z"/>
          <path d="M546 208h10l2 84h-14zM588 222h9l2 70h-13z"/>
          <path d="M620 234h30v18h-30zM618 234l17-9 17 9zM624 252h22l4 110h-30zM648 268a21 8 0 0 1 42 0v94h-42z"/>
        </g>
        <g fill="var(--lit)" opacity=".16"><path d="M380 246h4v116h-4zM448 250h4v112h-4zM508 270h4v20h-4zM612 268h4v94h-4zM686 268h4v94h-4zM363 214h4v32h-4z"/></g>
        <g fill="var(--lit)" opacity=".92"><circle cx="359" cy="226" r="3.5"/><path d="M404 264a4 4 0 0 1 8 0v13h-8z"/>{win30}</g>''',
  '<g fill="var(--lit)" opacity=".6"><rect class="lamp" style="--d:3.1s;--b:.5" x="1140" y="384" width="90" height="3" rx="1.5"/><rect class="lamp" style="--d:2.3s;--t:-1s;--b:.4" x="1160" y="392" width="54" height="3" rx="1.5"/><rect class="lamp" style="--d:3.7s;--t:-2s;--b:.5" x="1128" y="400" width="110" height="3" rx="1.5"/></g>'),
 STEAM,
 '''<g fill="none" stroke="var(--near)" stroke-width="1.5"><path d="M-10 384Q160 404 330 380Q485 402 640 380Q795 402 950 380Q1105 402 1260 380Q1430 402 1620 384"/><path d="M-10 392Q160 412 330 388Q485 410 640 388Q795 410 950 388Q1105 410 1260 388Q1430 410 1620 392"/></g>
        <g fill="var(--near)"><path d="M328 372h4v90h-4zM318 378h24v3h-24zM318 386h24v3h-24zM638 372h4v90h-4zM628 378h24v3h-24zM628 386h24v3h-24zM948 372h4v90h-4zM938 378h24v3h-24zM938 386h24v3h-24zM1258 372h4v90h-4zM1248 378h24v3h-24zM1248 386h24v3h-24z"/></g>''', 30)

a00 = [(244,242,36,100),(296,206,38,136),(350,250,48,90),(412,174,34,168),(460,220,42,120),(516,256,50,84),(580,230,26,110),(620,200,22,140)]
S2000 = wrap("An electric train on the same viaduct at midday, the town now a city of mid-rise blocks with a crane",
 back('''<circle cx="1260" cy="96" r="210" fill="url(#halo)"/><circle cx="1260" cy="96" r="50" fill="var(--lit)"/>
        <g class="drift" fill="#fff" opacity=".8"><rect x="640" y="92" width="170" height="28" rx="14"/><circle cx="690" cy="90" r="26"/><circle cx="742" cy="78" r="36"/><circle cx="784" cy="96" r="20"/></g>
        <g class="drift back" fill="#fff" opacity=".6"><rect x="90" y="150" width="120" height="20" rx="10"/><circle cx="126" cy="148" r="18"/><circle cx="162" cy="140" r="25"/></g>''',
  '',
  f'''<g class="bld">
          <path d="M240 236h44v124h-44zM290 200h10v-14h30v14h10v160h-50zM346 244h56v116h-56zM408 168h10v-22h22v22h10v192h-42zM428 116h2v30h-2zM456 214h50v146h-50zM512 250h58v110h-58zM576 224h34v136h-34zM616 196l30-18v182h-30z"/>
          <path d="M530 250v-74h3v74zM504 180h76v3h-76zM504 176h10v10h-10zM566 183h1.5v24h-1.5zM562 207h9v6h-9z"/>
        </g>
        <path d="M244 242h36v100h-36zM296 206h38v136h-38zM350 250h48v90h-48zM412 174h34v168h-34zM460 220h42v120h-42zM516 256h50v84h-50zM580 230h26v110h-26zM620 200h22v140h-22z" fill="url(#win)" opacity=".55"/>
        {togglers(a00, 3)}
        <circle class="lamp" style="--d:2s;--b:.1" cx="429" cy="116" r="2.2" fill="var(--accent)"/>
        <g fill="var(--lit)" opacity=".2"><path d="M280 236h4v124h-4zM336 200h4v160h-4zM398 244h4v116h-4zM446 168h4v192h-4zM502 214h4v146h-4zM566 250h4v110h-4zM606 224h4v136h-4zM642 180h4v180h-4z"/></g>''',
  '',
  '<rect y="220.6" width="1600" height="79.4" fill="url(#wire)"/>'),
 EMU, '', 22)

turb = lambda x, y, d: f'<g transform="translate({x} {y})"><rect x="-1.5" y="-66" width="3" height="66"/><g transform="translate(0 -66)"><g class="rot" style="animation-duration:9s;animation-delay:-{d}s"><circle r="37" fill="none"/><path d="M0 0l3-34h-6zM0 0l31 15-3 5zM0 0l-31 15 3 5z"/></g></g></g>'
a40 = [(250,166,34,160),(304,130,28,200),(354,186,48,140),(424,100,24,230),(470,150,40,180),(540,216,34,110),(602,170,22,160)]
stars = [(120,60,2),(210,140,1.3),(330,36,1.5),(540,24,1.2),(700,70,2),(790,150,1.2),(880,30,1.5),(1010,110,2),(1100,40,1.2),(1420,50,2),(1520,130,1.5),(640,130,1.5),(1360,150,1.2)]
S2040 = wrap("A sleek train with a strip of light crossing the viaduct at night under a skyline of lit towers",
 back('<g fill="var(--lit)">' + ''.join((lamp(f'<circle cx="{x}" cy="{y}" r="{r}"/>', .2) if i % 2 == 0 else f'<circle cx="{x}" cy="{y}" r="{r}"/>') for i, (x, y, r) in enumerate(stars)) + '''</g>
        <circle cx="1230" cy="92" r="170" fill="url(#halo)" opacity=".55"/><circle cx="1230" cy="92" r="36" fill="var(--lit)"/>''',
  '<g style="fill:color-mix(in oklab,var(--far) 70%,var(--ink))">' + turb(980, 214, 0) + turb(1060, 204, 2.2) + turb(1420, 200, 4.1) + '</g>',
  f'''<g class="bld"><rect x="244" y="150" width="46" height="210" rx="8"/><rect x="298" y="104" width="40" height="250" rx="20"/><rect x="346" y="172" width="64" height="180" rx="6"/><rect x="418" y="72" width="36" height="280" rx="18"/><rect x="462" y="136" width="56" height="220" rx="10"/><rect x="526" y="186" width="62" height="170" rx="31"/><rect x="596" y="158" width="34" height="190" rx="6"/><rect x="338" y="206" width="80" height="8"/><rect x="454" y="170" width="10" height="6"/><path d="M435 72h2v-30h-2zM317 104h2v-22h-2z"/></g>
        <g fill="url(#win)" opacity=".95"><rect x="250" y="166" width="34" height="160"/><rect x="304" y="130" width="28" height="200"/><rect x="354" y="186" width="48" height="140"/><rect x="424" y="100" width="24" height="230"/><rect x="470" y="150" width="40" height="180"/><rect x="540" y="216" width="34" height="110"/><rect x="602" y="170" width="22" height="160"/></g>
        {togglers(a40, 5)}
        <g fill="var(--accent)"><rect x="244" y="158" width="46" height="2"/><rect x="346" y="178" width="64" height="2"/><rect x="462" y="144" width="56" height="2"/><rect x="596" y="164" width="34" height="2"/><rect x="338" y="209" width="80" height="2"/><circle cx="436" cy="42" r="2.5"/><circle cx="318" cy="82" r="2.5"/></g>
        <g fill="url(#haloA)"><circle class="lamp" style="--d:2.2s;--b:.05" cx="436" cy="42" r="12"/><circle class="lamp" style="--d:2.2s;--t:-1.1s;--b:.05" cx="318" cy="82" r="12"/></g>''',
  '<g fill="var(--lit)" opacity=".45"><rect class="lamp" style="--d:3.3s;--b:.4" x="1200" y="384" width="60" height="3" rx="1.5"/><rect class="lamp" style="--d:2.6s;--t:-1s;--b:.4" x="1186" y="394" width="92" height="3" rx="1.5"/></g>'),
 MAGLEV, '', 14)

# ---- write index.html from the template -----------------------------------
here = os.path.dirname(os.path.abspath(__file__))
page = open(os.path.join(here, 'index.template.html'), encoding='utf-8').read()
for mark, block in (('<!--DEFS-->', DEFS), ('<!--SCENE:1930-->', S1930), ('<!--SCENE:2000-->', S2000), ('<!--SCENE:2040-->', S2040)):
    assert page.count(mark) == 1, mark
    page = page.replace(mark, block)
open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8', newline='\n').write(page)
print('index.html', len(page), 'bytes')
