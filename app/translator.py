import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from app import constants

load_dotenv()
api_key = os.getenv('LANGUAGE_TRANSLATOR_APIKEY')

authenticator = IAMAuthenticator(api_key)


language_translator = LanguageTranslatorV3(
        version=constants.LANGUAGE_TRANSLATOR_VERSION,
        authenticator=authenticator)
language_translator.set_service_url(constants.LANGUAGE_TRANSLATOR_URL)



def french_to_english(text: str):
    if not isinstance(text, str):
        print("Not a str")
        return None
    result = language_translator.translate(text=[text], model_id="fr-en").get_result()
    if result:
        translated_text = result['translations'][0]['translation']
        return translated_text


def english_to_french(text: str):
    if not isinstance(text, str):
        print("Not a str")
        return None
    result = language_translator.translate(text=[text], model_id="en-fr").get_result()
    if result:
        translated_text = result['translations'][0]['translation']
        print(translated_text)
        return translated_text


c = print(english_to_french("hello"))
print(c)