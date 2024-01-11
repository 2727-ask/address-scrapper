from bs4 import BeautifulSoup
import json

# HTML string containing the select options
html_string = '''
<select name="abbr" class="form-control">
<option value="0">Random</option>
<option value="al">Albania</option>
<option value="dz">Algeria</option>
<option value="ar">Argentina</option>
<option value="am">Armenia</option>
<option value="au">Australia</option>
<option value="at">Austria</option>
<option value="az">Azerbaijan</option>
<option value="bs">Bahamas</option>
<option value="bh">Bahrain</option>
<option value="bd">Bangladesh</option>
<option value="bb">Barbados</option>
<option value="by">Belarus</option>
<option value="be">Belgium</option>
<option value="bol">Bolivia</option>
<option value="bw">Botswana</option>
<option value="br">Brazil</option>
<option value="bn">Brunei</option>
<option value="kh">Cambodia</option>
<option value="cm">Cameroun</option>
<option value="ca">Canada</option>
<option value="ky">Cayman Islands</option>
<option value="cl">Chile</option>
<option value="cn">China</option>
<option value="co">Colombia</option>
<option value="cr">Costa Rica</option>
<option value="hr">Croatia</option>
<option value="cu">Cuba</option>
<option value="cy">Cyprus</option>
<option value="dk" selected="">Denmark</option>
<option value="do">Dominican Republic</option>
<option value="cd">DR Congo</option>
<option value="ec">Ecuador</option>
<option value="eg">Egypt</option>
<option value="sv">El Salvador</option>
<option value="ae">Emirates</option>
<option value="ee">Estonia</option>
<option value="et">Ethiopia</option>
<option value="fj">Fiji</option>
<option value="fi">Finland</option>
<option value="fr">France</option>
<option value="de">Germany</option>
<option value="gh">Ghana</option>
<option value="gt">Guatemala</option>
<option value="hn">Honduras</option>
<option value="hk">Hong Kong</option>
<option value="hu">Hungary</option>
<option value="in">India</option>
<option value="id">Indonesia</option>
<option value="ir">Iran</option>
<option value="ie">Ireland</option>
<option value="il">Israel</option>
<option value="it">Italy</option>
<option value="kt">Ivory Coast</option>
<option value="jm">Jamaica</option>
<option value="jp">Japan</option>
<option value="jo">Jordan</option>
<option value="kz">Kazakhstan</option>
<option value="ke">Kenya</option>
<option value="ko">Korea</option>
<option value="kw">Kuwait</option>
<option value="lv">Latvia</option>
<option value="lb">Lebanon</option>
<option value="ls">Lesotho</option>
<option value="ly">Libya</option>
<option value="lt">Lithuania</option>
<option value="lu">Luxembourg</option>
<option value="mg">Madagascar</option>
<option value="mw">Malawi</option>
<option value="my">Malaysia</option>
<option value="ml">Mali</option>
<option value="mt">Malta</option>
<option value="mu">Mauritius</option>
<option value="mx">México</option>
<option value="md">Moldova</option>
<option value="ma">Morocco</option>
<option value="mm">Myanmar</option>
<option value="na">Namibia</option>
<option value="np">Nepal</option>
<option value="nl">Netherlands</option>
<option value="nz">New Zealand</option>
<option value="ni">Nicaragua</option>
<option value="ng">Nigeria</option>
<option value="no">Norway</option>
<option value="om">Oman</option>
<option value="pk">Pakistan</option>
<option value="pa">Panamá</option>
<option value="pg">Papua New Guinea</option>
<option value="py">Paraguay</option>
<option value="pe">Perú</option>
<option value="ph">Philippines</option>
<option value="pl">Poland</option>
<option value="pt">Portuguese</option>
<option value="pr">Puerto Rico</option>
<option value="qa">Qatar</option>
<option value="ro">Romania</option>
<option value="ru">Russia</option>
<option value="rw">Rwanda</option>
<option value="sa">Saudi Arabia</option>
<option value="sn">Senegal</option>
<option value="sg">Singapore</option>
<option value="sk">Slovakia</option>
<option value="si">Slovenia</option>
<option value="za">South Africa</option>
<option value="es">Spain</option>
<option value="lk">Sri Lanka</option>
<option value="sr">Suriname</option>
<option value="se">Sweden</option>
<option value="ch">Switzerland</option>
<option value="tw">Taiwan(China)</option>
<option value="tz">Tanzania</option>
<option value="th">Thailand</option>
<option value="cz">The Czech Republic</option>
<option value="is">The Republic of Iceland</option>
<option value="tt">Trinidad and Tobago</option>
<option value="tn">Tunisia</option>
<option value="tr">Turkey</option>
<option value="ug">Uganda</option>
<option value="ua">Ukraine</option>
<option value="uk">United Kingdom</option>
<option value="us">United States</option>
<option value="uy">Uruguay</option>
<option value="uz">Uzbekistan</option>
<option value="ve">Venezuela</option>
<option value="vn">Vietnam</option>
<option value="ye">Yemen</option>
<option value="zm">Zambia</option>
<option value="zw">Zimbabwe</option>
<option value="kg">Киргизия</option>
</select>
'''

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_string, 'html.parser')

# Find all option elements within the select tag
options = soup.find_all('option')

# Create a dictionary to store the values and texts
country_dict = {}

# Loop through the options and add them to the dictionary
for option in options:
    value = option.get('value')
    text = option.text.strip()
    country_dict[value] = text

# Convert the dictionary to a JSON object
    
file_name = 'cc.json'

with open(file_name, 'w') as file:
    json.dump(country_dict, file, indent=4)
  

