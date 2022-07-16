from pyrogram import Client, filters
from plugins.helper_functions.basic_helpers import edit_or_reply, get_text
import flag
import html
from countryinfo import CountryInfo



@Client.on_message(filters.command("Countries"))
async def country_(client, message):
    msg_ = await edit_or_reply(message, "`Searching For Country.....`")
    lol = get_text(message)
    if not lol:
        await msg_.edit("`Please Give Input!`")
        return
    country = CountryInfo(lol)
    try:
        a = country.info()
    except:
        await msg_.edit("`Country Not Found. Maybe You Need to Learn Geography!`")
        return
    name = a.get("name")
    bb = a.get("altSpellings")
    hu = "".join(p + ",  " for p in bb)
    area = a.get("area")
    hell = a.get("borders")
    borders = "".join(fk + ",  " for fk in hell)
    WhAt = a.get("callingCodes")
    call = "".join(what + "  " for what in WhAt)
    capital = a.get("capital")
    fker = a.get("currencies")
    currencies = "".join(FKer + ",  " for FKer in fker)
    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR = PAblo.get("type")
    iso = ""
    iSo = a.get("ISO")
    for hitler in iSo:
      po = iSo.get(hitler)
      iso += po + ",  "
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)
    languages = a.get("languages")
    lMAO = "".join(lmao + ",  " for lmao in languages)
    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom = "".join(jerry + ",   " for jerry in tik)
    GOT = a.get("tld")
    lanester = "".join(targaryen + ",   " for targaryen in GOT)
    wiki = a.get("wiki")
    caption = f"""<b><u>information gathered successfully</b></u>
<b>
Country Name:- {name}
Alternative Spellings:- {hu}
Country Area:- {area} square kilometers
Borders:- {borders}
Calling Codes:- {call}
Country's Capital:- {capital}
Country's currency:- {currencies}
Country's Flag:- {okie}
Demonym:- {HmM}
Country Type:- {EsCoBaR}
ISO Names:- {iso}
Languages:- {lMAO}
Native Name:- {nonive}
population:- {waste}
Region:- {reg}
Sub Region:- {sub}
Time Zones:- {tom}
Top Level Domain:- {lanester}
wikipedia:- {wiki}</b>
<u><b>
Information Gathered By FridayUB.
"""
    await msg_.edit(caption, parse_mode="html", disable_web_page_preview=True)
