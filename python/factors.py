def find_factors(number):
 factors= []
 for i in range(1,number +1):
  if number % i==0:
      factors.append(i)
      return factors
 your_number=20
 result=find_factors(your_number)
 print(f"factors of the{your_number} are:{result}")
 
