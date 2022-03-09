import Data.Binary.Put (putInt8)
addOne arg = 1+arg
four = addOne 3


main = print four