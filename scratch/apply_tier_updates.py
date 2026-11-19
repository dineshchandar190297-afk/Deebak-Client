import re

path = r"c:\Users\dines\Downloads\Deebak Client\utils\ai.ts"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Pronunciation prompt
old_pron_prompt = """  If ${level} includes "Beginner", use simple 1-2 word common phrases (e.g. Hello, Thank you, Water).
  If ${level} includes "Intermediate", use conversational sentences with 3-5 words (e.g. I am going to the store).
  If ${level} includes "Pro" or "Advanced", use tough tongue-twisters, complex grammatical sentences, or advanced cultural idioms with 5-10 words."""

new_pron_prompt = """  If ${level} includes "Beginner", use alphabets, consonants, vowels, and simple 1-2 word basic words (e.g. Mother, Water, Cat).
  If ${level} includes "Intermediate", use tough words and short 3-5 word sentences (e.g. The cat plays in garden).
  If ${level} includes "Pro" or "Advanced", use typical complex sentences, advanced grammar, and long 5-10+ word sentences."""

content = content.replace(old_pron_prompt, new_pron_prompt)

# Replace Practice lesson prompt
old_prac_prompt = """  CRITICAL DIFFICULTY INSTRUCTIONS:
  - If ${level} includes "Beginner", make the exercises very simple, using basic, common words and short sentences.
  - If ${level} includes "Intermediate", use conversational grammar and moderate vocabulary.
  - If ${level} includes "Pro" or "Advanced", use extremely tough and highly advanced vocabulary. Every single word and scenario must be very challenging, including rare words, complex grammar, and difficult literary terms."""

new_prac_prompt = """  CRITICAL DIFFICULTY INSTRUCTIONS:
  - If ${level} includes "Beginner", focus on alphabets, consonants, vowels, and simple 1-2 word basic words.
  - If ${level} includes "Intermediate", focus on tough words and short 3-5 word sentences.
  - If ${level} includes "Pro" or "Advanced", focus on typical sentences, complex grammar, and long 5-10+ word sentences."""

content = content.replace(old_prac_prompt, new_prac_prompt)

# Replace Flashcard lesson prompt
old_flash_prompt = """  DIFFICULTY:
  - "Beginner": simple nouns (animals, food, colors, family) or basic verbs.
  - "Intermediate": intermediate phrases, emotions, weather, or conversational terms.
  - "Pro" or "Advanced": EXTREMELY TOUGH vocabulary. Every single word must be highly advanced, rare, difficult professional terms, obscure idioms, or complex abstract concepts. No simple words allowed!"""

new_flash_prompt = """  DIFFICULTY:
  - "Beginner": alphabets, consonants, vowels, and simple 1-2 word basic words.
  - "Intermediate": tough words and short 3-5 word sentences.
  - "Pro" or "Advanced": typical sentences, complex grammar, and long 5-10+ word sentences."""

content = content.replace(old_flash_prompt, new_flash_prompt)

# Replace Reading lesson prompt
old_read_prompt = """  CRITICAL DIFFICULTY INSTRUCTIONS: 
  - If ${level} includes "Beginner", write 3-4 very simple sentences about daily life, animals, or food.
  - If ${level} includes "Intermediate", write a short paragraph about a cultural event or a trip with moderate vocabulary.
  - If ${level} includes "Pro", write a complex story, folk tale, or article with advanced grammar and idioms."""

new_read_prompt = """  CRITICAL DIFFICULTY INSTRUCTIONS: 
  - If ${level} includes "Beginner", focus on alphabets, consonants, vowels, and simple 1-2 word basic words in 2-3 short sentences.
  - If ${level} includes "Intermediate", write short stories with tough words and 3-5 word sentences.
  - If ${level} includes "Pro" or "Advanced", write longer stories with typical complex sentences, advanced grammar, and literary phrases."""

content = content.replace(old_read_prompt, new_read_prompt)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated utils/ai.ts with strict Tier rules!")
