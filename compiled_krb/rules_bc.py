# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def what_to_bring_lightweight_waterproof_jacket(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_bring_lightweight_waterproof_jacket: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_bring_lightweight_waterproof_jacket: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_sunny', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_bring_lightweight_waterproof_jacket: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_umbrella(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_bring_umbrella: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_bring_umbrella: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_sunny', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_bring_umbrella: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_raincoat(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_bring_raincoat: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_bring_raincoat: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_sunny', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_bring_raincoat: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_cap(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_bring_cap: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_bring_cap: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_sunny', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_bring_cap: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_hoodie(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_bring_hoodie: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_bring_hoodie: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_sunny', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_bring_hoodie: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_sunglasses(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_bring_sunglasses: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_bring_sunglasses: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_sunny', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_bring_sunglasses: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_jacket(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_bring_jacket: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_bring_jacket: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_sunny', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_bring_jacket: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_lightweight_sweater(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_raining', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_bring_lightweight_sweater: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_windy', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_bring_lightweight_sweater: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_sunny', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_bring_lightweight_sweater: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('what_to_bring_lightweight_waterproof_jacket', This_rule_base, 'what_to_bring',
                  what_to_bring_lightweight_waterproof_jacket, None,
                  (pattern.pattern_literal('lightweight_waterproof_jacket'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_umbrella', This_rule_base, 'what_to_bring',
                  what_to_bring_umbrella, None,
                  (pattern.pattern_literal('umbrella'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_raincoat', This_rule_base, 'what_to_bring',
                  what_to_bring_raincoat, None,
                  (pattern.pattern_literal('raincoat'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_cap', This_rule_base, 'what_to_bring',
                  what_to_bring_cap, None,
                  (pattern.pattern_literal('cap'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_hoodie', This_rule_base, 'what_to_bring',
                  what_to_bring_hoodie, None,
                  (pattern.pattern_literal('hoodie'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_sunglasses', This_rule_base, 'what_to_bring',
                  what_to_bring_sunglasses, None,
                  (pattern.pattern_literal('sunglasses'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_jacket', This_rule_base, 'what_to_bring',
                  what_to_bring_jacket, None,
                  (pattern.pattern_literal('jacket'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_lightweight_sweater', This_rule_base, 'what_to_bring',
                  what_to_bring_lightweight_sweater, None,
                  (pattern.pattern_literal('lightweight_sweater'),),
                  (),
                  (pattern.pattern_literal(False),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((26, 31), (5, 5)),
    ((32, 37), (6, 6)),
    ((50, 54), (9, 9)),
    ((56, 61), (11, 11)),
    ((62, 67), (12, 12)),
    ((68, 73), (13, 13)),
    ((86, 90), (16, 16)),
    ((92, 97), (18, 18)),
    ((98, 103), (19, 19)),
    ((104, 109), (20, 20)),
    ((122, 126), (23, 23)),
    ((128, 133), (25, 25)),
    ((134, 139), (26, 26)),
    ((140, 145), (27, 27)),
    ((158, 162), (30, 30)),
    ((164, 169), (32, 32)),
    ((170, 175), (33, 33)),
    ((176, 181), (34, 34)),
    ((194, 198), (37, 37)),
    ((200, 205), (39, 39)),
    ((206, 211), (40, 40)),
    ((212, 217), (41, 41)),
    ((230, 234), (44, 44)),
    ((236, 241), (46, 46)),
    ((242, 247), (47, 47)),
    ((248, 253), (48, 48)),
    ((266, 270), (51, 51)),
    ((272, 277), (53, 53)),
    ((278, 283), (54, 54)),
    ((284, 289), (55, 55)),
)
