from numpy import finfo, float64, float32
print("attributes you can access in finfo(float64) ", dir(finfo(float64)))
print( "maximum numbers in 64 bit and 32 bit precision: ", finfo(float64).max,
      finfo(float32).max)
print( "minimum numbers in 64 bit and 32 bit precision: ", finfo(float64).min, 
      finfo(float32).min)
print( "epsilon for 64 bit and 32 bit: ", finfo(float64).eps, 
      finfo(float32).eps)
print( "Should be epsilon for this machine if it's 64 bit",
      float64(1)+finfo(float64).eps-float64(1))
print( "Should be zero", float64(1)+finfo(float64).eps/2.0-float64(1))

