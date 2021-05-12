# -*- coding: utf-8 -*-
"""
Created on Wed May 12 08:10:00 2021
@author: Swapnanil Sharma, https://github.com/swapnanilsharma
"""


import tensorflow as tf
from transformers import BertTokenizer
from transformers import TFBertForQuestionAnswering

'''
A Simple library created using BERT and HuggingFace finetunning.
Original paper :https://arxiv.org/abs/1810.04805
Source code for BERT by Google Research:https://github.com/google-research/bert/
The base code wrapper is taken from https://huggingface.co/bert-large-uncased-whole-word-masking-finetuned-squad
'''


class QuestionAnsweringBERT():

    def __init__(self, modelName="bert-large-uncased-whole-word-masking-finetuned-squad"):
        self.modelName = modelName
        self.model = TFBertForQuestionAnswering.from_pretrained(self.modelName)
        self.tokenizer = BertTokenizer.from_pretrained(modelName)

    def getAns(self, paragraph, question):
        self.question = question
        self.paragraph = paragraph
        self.question = question

        input_text =  question + " [SEP] " + paragraph 
        input_ids = self.tokenizer.encode(input_text)
        input1 = tf.constant(input_ids)[None, :]
        token_type_ids = [0 if i <= input_ids.index(102) else 1 for i in range(len(input_ids))]
        answer=self.model(input1, token_type_ids = tf.convert_to_tensor([token_type_ids]))
        startScores, endScores = answer
        input_tokens = self.tokenizer.convert_ids_to_tokens(input_ids)
        startIdx = tf.math.argmax(startScores[0],0).numpy()
        endIdx = tf.math.argmax(endScores[0],0).numpy()+1
        answer = " ".join(input_tokens[startIdx:endIdx])
        answer = answer.replace("##", "")
        return answer