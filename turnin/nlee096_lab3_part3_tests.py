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
        #000
        {'description': ' PORTA = 0x00 => PORTC = 0x40',
         'steps': [ {'inputs': [('PINA', 0x00)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x40)],
        },
        #001
        {'description': ' PORTA = 0x10 => PORTC = 0x40',
         'steps': [ {'inputs': [('PINA', 0x10)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x40)],
        },
        #010
        {'description': ' PORTA = 0x20 => PORTC = 0x40',
         'steps': [ {'inputs': [('PINA', 0x20)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x40)],
        },
        #011
        {'description': ' PORTA = 0x30 => PORTC = 0xC0',
         'steps': [ {'inputs': [('PINA', 0x30)], 'iterations': 1 } ],
         'expected': [('PORTC', 0xC0)],
        },
        #100
        {'description': ' PORTA = 0x40 => PORTC = 0x40',
         'steps': [ {'inputs': [('PINA', 0x40)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x40)],
        },
        #101
        {'description': ' PORTA = 0x50 => PORTC = 0x40',
         'steps': [ {'inputs': [('PINA', 0x50)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x40)],
        },
        #110
        {'description': ' PORTA = 0x60 => PORTC = 0x40',
         'steps': [ {'inputs': [('PINA', 0x60)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x40)],
        },
        #111
        {'description': ' PORTA = 0x70 => PORTC = 0x40',
         'steps': [ {'inputs': [('PINA', 0x70)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x40)],
        },
    #1
        #000
        {'description': ' PORTA = 0x01 => PORTC = 0x60',
         'steps': [ {'inputs': [('PINA', 0x01)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x60)],
        },
        #001
        {'description': ' PORTA = 0x11 => PORTC = 0x60',
         'steps': [ {'inputs': [('PINA', 0x11)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x60)],
        },
        #010
        {'description': ' PORTA = 0x21 => PORTC = 0x60',
         'steps': [ {'inputs': [('PINA', 0x21)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x60)],
        },
        #011
        {'description': ' PORTA = 0x31 => PORTC = 0xE0',
         'steps': [ {'inputs': [('PINA', 0x31)], 'iterations': 1 } ],
         'expected': [('PORTC', 0xE0)],
        },
        #100
        {'description': ' PORTA = 0x41 => PORTC = 0x60',
         'steps': [ {'inputs': [('PINA', 0x41)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x60)],
        },
        #101
        {'description': ' PORTA = 0x51 => PORTC = 0x60',
         'steps': [ {'inputs': [('PINA', 0x51)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x60)],
        },
        #110
        {'description': ' PORTA = 0x61 => PORTC = 0x60',
         'steps': [ {'inputs': [('PINA', 0x61)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x60)],
        },
        #111
        {'description': ' PORTA = 0x71 => PORTC = 0x60',
         'steps': [ {'inputs': [('PINA', 0x71)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x60)],
        },

    #7
        {'description': ' PORTA = 0x07 => PORTC = 0x3C',
         'steps': [ {'inputs': [('PINA', 0x07)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3C)],
        },
        #001
        {'description': ' PORTA = 0x17 => PORTC = 0x3C',
         'steps': [ {'inputs': [('PINA', 0x17)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3C)],
        },
        #010
        {'description': ' PORTA = 0x27 => PORTC = 0x3C',
         'steps': [ {'inputs': [('PINA', 0x27)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3C)],
        },
        #011
        {'description': ' PORTA = 0x37 => PORTC = 0xBC',
         'steps': [ {'inputs': [('PINA', 0x37)], 'iterations': 1 } ],
         'expected': [('PORTC', 0xBC)],
        },
        #100
        {'description': ' PORTA = 0x47 => PORTC = 0x3C',
         'steps': [ {'inputs': [('PINA', 0x47)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3C)],
        },
        #101
        {'description': ' PORTA = 0x57 => PORTC = 0x3C',
         'steps': [ {'inputs': [('PINA', 0x57)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3C)],
        },
        #110
        {'description': ' PORTA = 0x67 => PORTC = 0x3C',
         'steps': [ {'inputs': [('PINA', 0x67)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3C)],
        },
        #111
        {'description': ' PORTA = 0x77 => PORTC = 0x3C',
         'steps': [ {'inputs': [('PINA', 0x77)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3C)],
        },

    #15
        {'description': ' PORTA = 0x0F => PORTC = 0x3F',
         'steps': [ {'inputs': [('PINA', 0x0F)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3F)],
        },
        #001
        {'description': ' PORTA = 0x1F => PORTC = 0x3F',
         'steps': [ {'inputs': [('PINA', 0x1F)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3F)],
        },
        #010
        {'description': ' PORTA = 0x2F => PORTC = 0x3F',
         'steps': [ {'inputs': [('PINA', 0x2F)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3F)],
        },
        #011
        {'description': ' PORTA = 0x3F => PORTC = 0xBF',
         'steps': [ {'inputs': [('PINA', 0x3F)], 'iterations': 1 } ],
         'expected': [('PORTC', 0xBF)],
        },
        #100
        {'description': ' PORTA = 0x4F => PORTC = 0x3F',
         'steps': [ {'inputs': [('PINA', 0x4F)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3F)],
        },
        #101
        {'description': ' PORTA = 0x5F => PORTC = 0x3F',
         'steps': [ {'inputs': [('PINA', 0x5F)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3F)],
        },
        #110
        {'description': ' PORTA = 0x6F => PORTC = 0x3F',
         'steps': [ {'inputs': [('PINA', 0x6F)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3F)],
        },
        #111
        {'description': ' PORTA = 0x7F => PORTC = 0x3F',
         'steps': [ {'inputs': [('PINA', 0x7F)], 'iterations': 1 } ],
         'expected': [('PORTC', 0x3F)],
        },

    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']

