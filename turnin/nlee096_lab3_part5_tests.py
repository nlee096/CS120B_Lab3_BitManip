# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ 
    # {'description': 'This test will run first.',
    # 'steps': [ {'inputs': [('PINA',<val>)], 'iterations': 1 } ],
    # 'expected': [('PORT',<val>)],
    # },
    # {'description': 'This test will run second.',
    # 'steps': [ {'inputs': [('PIN', <val>)],'iterations': 1}, # Set PIN to val then run one iteration
    #     {'inputs': [('PIN',<val>)], 'time': 300 }, # Set PIN to val then run 300 ms
    #     {'inputs': [('PIN',<val>)], 'iterations': 1, 'expected': [('PORT',<val>)]}, 
    #     {'inputs': [('PIN',<val>)], 'time': 600}, ],
    # 'expected': [('PORT',<val>)],
    # },

       
    #0
    {'description': '() PORTD = 0x00, PORTB = 0x00, PORTC = 0x00',
     'steps': [ {'inputs': [('PIND', 0x00), ('PINB', 0x00)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x00)],
    },

    #2
    {'description': '() PORTD = 0x01, PORTB = 0x00, PORTC = 0x00',
     'steps': [ {'inputs': [('PIND', 0x01), ('PINB', 0x00)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x00)],
    },

    #6
    {'description': '() PORTD = 0x03, PORTB = 0x00, PORTC = 0x00',
     'steps': [ {'inputs': [('PIND', 0x03), ('PINB', 0x00)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x04)],
    },

    #10
    {'description': '() PORTD = 0x05, PORTB = 0x00, PORTC = 0x00',
     'steps': [ {'inputs': [('PIND', 0x05), ('PINB', 0x00)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x04)],
    },

    #14
    {'description': '() PORTD = 0x07, PORTB = 0x00, PORTC = 0x04',
     'steps': [ {'inputs': [('PIND', 0x07), ('PINB', 0x00)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x04)],
    },

    #70
    {'description': '() PORTD = 0x23, PORTB = 0x00, PORTC = 0x04',
     'steps': [ {'inputs': [('PIND', 0x23), ('PINB', 0x00)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x02)],
    },

    #140
    {'description': '() PORTD = 0x46, PORTB = 0x00, PORTC = 0x02',
     'steps': [ {'inputs': [('PIND', 0x46), ('PINB', 0x00)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x02)],
    },

    #510
    {'description': '() PORTD = 0xFF, PORTB = 0x00, PORTC = 0x02',
     'steps': [ {'inputs': [('PIND', 0xFF), ('PINB', 0x00)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x02)],
    },

    #1
    {'description': '() PORTD = 0x00, PORTB = 0x01, PORTC = 0x02',
     'steps': [ {'inputs': [('PIND', 0x00), ('PINB', 0x01)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x00)],
    },

    #257
    {'description': '() PORTD = 0x80, PORTB = 0x01, PORTC = 0x02',
     'steps': [ {'inputs': [('PIND', 0x80), ('PINB', 0x01)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x02)],
    },

    #273
    {'description': '() PORTD = 0x88, PORTB = 0x01, PORTC = 0x02',
     'steps': [ {'inputs': [('PIND', 0x88), ('PINB', 0x01)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x02)],
    },

    #511
    {'description': '() PORTD = 0xFF, PORTB = 0x01, PORTC = 0x02',
     'steps': [ {'inputs': [('PIND', 0xFF), ('PINB', 0x01)], 'iterations': 1 } ],
     'expected': [('PORTB', 0x02)],
    },

    # {'description': '() PORTD = 0x00, PORTB = 0x00, PORTC = 0x00',
    #  'steps': [ {'inputs': [('PIND', 0x00), ('PINB', 0x00)], 'iterations': 1 } ],
    #  'expected': [('PORTB', 0x00)],
    # },


    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']

