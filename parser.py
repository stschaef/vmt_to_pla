from pyparsing import *
import pprint
from sympy import Integer

declare_sort = Literal("declare-sort")
define_fun = Literal("define-fun")
declare_fun = Literal("declare-fun")

left_paren = Literal("(").suppress()
right_paren = Literal(")").suppress()

symbol = Word(alphanums+'_.:')
arguments = Group(ZeroOrMore(symbol))
return_type = Literal("Bool")
arity = Word(nums)
fun_defn_args = Group(ZeroOrMore(left_paren + symbol + symbol + right_paren))
annotation = Literal(":next") | Literal(":invar-property") | Literal(":trans") | Literal(":action")
annotation_target = left_paren + Group(symbol + OneOrMore(symbol)) + right_paren | symbol
annotation_term = Group(left_paren + Literal("!") + annotation_target + annotation + symbol + right_paren)


sort_decl = Group(left_paren + declare_sort + symbol + arity + right_paren)
fun_decl = Group(left_paren + declare_fun + symbol + left_paren + arguments + right_paren + return_type + right_paren)
fun_defn = Group(left_paren + define_fun + symbol + left_paren + fun_defn_args + right_paren + return_type + annotation_term + right_paren)
term = sort_decl | fun_decl | fun_defn

code = OneOrMore(term)

# f = open("lockserv_automaton.vmt", "r")

# vmt_code = "".join(f.read().split('\n'))
# print(vmt_code)
s = """
(define-fun .held () Bool (! __held :next held))
(define-fun .grant_msg ((V0 node)) Bool (! (__grant_msg V0) :next grant_msg))
(define-fun .holds_lock ((V0 node)) Bool (! (__holds_lock V0) :next holds_lock))
(define-fun .lock_msg ((V0 node)) Bool (! (__lock_msg V0) :next lock_msg))
(define-fun .unlock_msg ((V0 node)) Bool (! (__unlock_msg V0) :next unlock_msg))
"""
print(code.parseString(s))

# print(code.parseString("(declare-sort node 0) (define-fun .node ((S node)) node (! S :sort 2))").asList())
# print("".join(f.readlines()))

# print()