from pyke import knowledge_engine

engine = knowledge_engine.engine(__file__)

engine.reset()

engine.activate('rules')

try:
  with engine.prove_goal('rules.what_to_bring($bring)') as gen:
    for vars, plan in gen:
      print(f'You should bring: {vars["bring"]}') 
except Exception:
  print(Exception)


