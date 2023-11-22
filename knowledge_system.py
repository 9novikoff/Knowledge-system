import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)
    
def what_to_bring_questions():

    engine.reset()   

    engine.activate('rules')
    
    try:
        with engine.prove_goal('rules.what_to_bring($bring)') as gen: 
            for vars, plan in gen:
                print("You should bring: %s" % (vars['bring']))

    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    print()

what_to_bring_questions()