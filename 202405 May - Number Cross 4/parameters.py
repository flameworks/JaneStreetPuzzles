PARAMS = [  
            [0,0,0,4,4,4,8,8,9,9,9   ], # Row 1
            [0,3,3,3,4,4,8,9,9,9,10  ], # Row 2
            [0,3,3,4,4,4,8,9,9,9,10  ], # Row 3
            [0,3,3,4,4,5,5,9,10,10,10], # Row 4 sum of digits 7
            [0,3,4,4,9,9,5,9,10,11,10], # Row 5 
            [0,9,9,9,9,9,9,9,11,11,12], # Row 6
            [2,9,9,9,9,6,6,9,11,11,11], # Row 7, multiple of 37
            [2,2,1,9,1,6,6,9,9,11,9, ], # Row 8 ##### LOW RESULTS
            [2,2,1,1,1,6,6,9,9,9,9,  ], # Row 9, product ends in 1
            [2,1,1,2,2,2,6,9,9,9,7,  ], # Row 10, multiple of 88
            [2,2,2,2,2,6,6,6,9,9,7,  ], # Row 11
         ]

CONSTRAINTS = [
                "derive_squares.json"   , # Row 1
                "palindrome_p1.json"    , # Row 2
                "prime_power.json"      , # Row 3
                ""                      , # Row 4 sum of digits 7 @@@@@@@@@@@@@@@@ sample
                "fibonacci.json"        , # Row 5 
                "derive_squares.json"   , # Row 6
                ""                      , # Row 7, multiple of 37 @@@@@@@@@@@@@@@@ sample
                "palindrome_23.json"    , # Row 8 
                ""                      , # Row 9, product ends in 1
                ""                      , # Row 10, multiple of 88
                "palindrome_m1.json"    , # Row 11
              ]

WORD_CONSTANTS = [
                    "Square"                , # Row 1
                    "1 more than Pall"      , # Row 2
                    "prime power prime"     , # Row 3
                    "Sum digits 7"          , # Row 4 sum of digits 7 
                    "Fibonacci"             , # Row 5 
                    "Square"                , # Row 6
                    "Multiple of 37"        , # Row 7, multiple of 37 
                    "Pall and %23"          , # Row 8 
                    "Product ends 1"        , # Row 9, product ends in 1
                    "Multiple of 88"        , # Row 10, multiple of 88
                    "1 less than Pall"      , # Row 11
                 ]

MASTER_NUM = len(PARAMS[0])