'''
@Author: zhaoyang.liang
@Github: https://github.com/LzyRapx
@Date: 2020-02-01 16:29:08
'''
import time
from base import _is_square, _factorial, fac
from base import _iroot, cprod, ggcd
from base import extended_gcd

print(_is_square(8))
print(_is_square(9))
print(_factorial(4))
print(fac(10))
print(_iroot(10,1)) # (10, True)
print(_iroot(10,2)) # (3, False)
print(cprod([2,3,5,6]))
print(cprod([2,3,5,7,11,12]))

print(ggcd([11,22,33]))

print(extended_gcd(3,6)) #  3*x + 6*y = gcd(3, 6) => (gcd(3,6), x, y) => (3,1,0)

from base import padic_base_p
print(padic_base_p(10,2)) # 1010
print(padic_base_p(10,3)) # 101

from base import iter_associate, sum_power_series_mod
def f(a, b):
    s = 1
    for i in range(1, a):
        s *= i
    print("a = {} b = {} s = {} ".format(a, b, s))
    return s
print(iter_associate(f, 4, 3)) # 120
print(sum_power_series_mod(1,100,19260817))

from base import rational_continous_frac
print(rational_continous_frac(415,93,10000)) # (4,2,6,7)

from base import continous_frac_convergent
print(continous_frac_convergent([4,2,6,7])) # [Fraction(4, 1), Fraction(9, 2), Fraction(58, 13), Fraction(415, 93)]
print(float(continous_frac_convergent([4,2,6,7])[2]))


from treeGeneration import pythagorean_triple_tree
print(pythagorean_triple_tree())
print(pythagorean_triple_tree((5,12,13),forward=False, trust=True))

from treeGeneration import stern_brocot_tree
res = stern_brocot_tree()
print("test...")
# while True:
#     g = next(res)
#     print(g)
#     if g[0] == 1 and g[1] == 4:
#         print(g)
#         break
#     time.sleep(1)
# print("stern_brocot_tree: ", next(res))

#########################################
from prime import _primes_list, _is_prime, _mobius_list
p = _primes_list(100)
print(p)

Is_p = _is_prime(97)
print(Is_p)

mobius_list = _mobius_list(100)
print(len(mobius_list))
print(mobius_list[0])
print(mobius_list[100])

from prime import _pollard_rho,prime_divisor_decomposition, all_divisors
print(_pollard_rho(1000))
print(prime_divisor_decomposition(10**12+2000))
print(all_divisors(10 ** 9))

from prime import euler_phi, mobius, _largest_prime_factor_sieve,prime_counting
for i in range(1, 100):
    print(euler_phi(i), end=" ")
print()
for i in range(1, 100):
    print(mobius(i), end=" ")
print()
print(_largest_prime_factor_sieve(18))
print(_largest_prime_factor_sieve(25))
print(prime_counting(10 ** 5))

###############################################
from combinatoric import C, C_mod, permutations_multiset
from combinatoric import list_multiset_permutations
print(C(4,2))
print(C_mod(4,2,11))
print(C_mod(1000000, 123123, 10 ** 9 + 7))
print(permutations_multiset([1,2]))
print(permutations_multiset([1,1]))


print(permutations_multiset([1,1,1]))
for lists in list_multiset_permutations([1,2,3]):
    print(lists)



