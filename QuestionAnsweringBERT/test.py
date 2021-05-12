# -*- coding: utf-8 -*-
"""
Created on Wed May 12 08:10:00 2021
@author: Swapnanil Sharma, https://github.com/swapnanilsharma
"""

import QuestionAnsweringBERT as qabert
import warnings
warnings.filterwarnings("ignore")

'''
This is a sample example of checking how we are getting answers based on one paragraph and a question.
This takes as inputs 1 paragraph (maximum 512 words of length) annd one question.
The QuestionAnsweringBERT() is the method to get the answer
'''

if __name__=='__main__':
    paragraph = r"""Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).
It was first identified in December 2019 in Wuhan, Hubei, China, and has resulted in an ongoing pandemic. 
As of 5 October 2020, more than 35 million cases have been reported across 188 countries and territories with more than 1.03 million deaths; more than 24.4 million people have recovered.
Common symptoms include fever, cough, fatigue, shortness of breath or breathing difficulties, and loss of smell and taste.
While most people have mild symptoms, some people develop acute respiratory distress syndrome (ARDS) possibly precipitated by cytokine storm, multi-organ failure, septic shock, and blood clots. 
The incubation period may range from one to fourteen days.
The disease spreads most often when people are physically close.
It spreads very easily and sustainably through the air, primarily via small droplets and sometimes in aerosols, as an infected person breathes, coughs, sneezes, talks, or sings.
It may also be transmitted via contaminated surfaces, although this has not been conclusively demonstrated.
It can spread for up to two days prior to symptom onset and from people who are asymptomatic.
The standard method of diagnosis is by real-time reverse transcription polymerase chain reaction (rRT-PCR) from a nasopharyngeal swab. 
Chest CT imaging may also be helpful for diagnosis in individuals where there is a high suspicion of infection based on symptoms and risk factors, however guidelines do not recommend using it for routine screening.
Recommended measures to prevent infection include frequent hand washing, social distancing, quarantine, covering coughs and sneezes, and keeping unwashed hands away from the face.
The use of face masks or cloth face coverings such as a scarf or a bandana has been recommended by health officials in public settings to minimise the risk of transmissions, with some authorities requiring their use in certain settings, such as on public transport and in shops. 
Health officials also stated that medical-grade face masks, such as N95 masks, should be used only by healthcare workers, first responders, and those who directly care for infected individuals.
There are no proven vaccines or specific treatments for COVID-19 yet, though several are in development."""
    question='What is Coronavirus?'
    qabert=qabert.QuestionAnsweringBERT()
    ans=qabert.getAns(paragraph=paragraph, question=question)
    print(ans)