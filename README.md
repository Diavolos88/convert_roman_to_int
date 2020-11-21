# convert_roman_to_int
# Test solution for Napoleon IT
Задание состоит в следующем:

Римские цифры представлены в виде I, V, X, L, C, D и M
Необходимо с помощью кода python преобразовать римское число в арабское (стандартное) число.

Пример 1:
Input: s = "III"
Output: 3

Пример 2:
Input: s = "IV"
Output: 4

Пример 3:
Input: s = "IX"
Output: 9

Пример 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Пример 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Условия:
1. Длина 1 <= s.length <= 15
2. s состоит только из ('I', 'V', 'X', 'L', 'C', 'D', 'M')
3. Гарантируется, что конвертируемая в число s будет в диапозоне [1, 3999]

4. Необходимо написать решение если дан следующий python код
class Solution:
def romanToInt(self, s: str) -> int:

5. Не используй сторонние библиотеки (код должен быть написан на pure python)

7. Решение вышли в виде ссылки на репозиторий GitHub, имя файла - любое, но с расширением .py
