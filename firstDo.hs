main = do putStrLn "What is 4*5?"
          x <- readLn 
          if x == 20
            then putStrLn "Correct"
            else putStrLn "Wrong"