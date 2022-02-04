#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()

my_cache.put("E", "School")
my_cache.print_cache()

my_cache.put("A", "Mundo en español")
my_cache.print_cache()

my_cache.put("F", "New word")
my_cache.print_cache()

my_cache.put("H", "Hello")
my_cache.print_cache()

my_cache.put("G", "Hello")
my_cache.print_cache()

print(my_cache.get("G"))
