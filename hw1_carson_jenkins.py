{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNNkj1THB/Yft+cuyvoxNbO"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3etLyX9r2-ux",
        "outputId": "a65dd3a1-81d2-42df-9f21-2002d3a9b202"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1. Square\n",
            "2. Triangle\n",
            "\n",
            "Which do you want the area for? 1\n",
            "Length of side: 5\n",
            "Compute area of square with side length 5: 25\n",
            "82 % 1 = 0\n",
            "0\n",
            "92 - 2 = 90\n",
            "90\n",
            "Disregard decimal remainder: \n",
            "96 // 3 = 32\n",
            "32\n",
            "You completed the security quiz. Here are all of your passwords: \n",
            "jdajs998fd\n",
            "34neJnf34\n",
            "pswd145unlck23\n",
            "013003Uo\n"
          ]
        }
      ],
      "source": [
        "'''\n",
        "Homework 1\n",
        "Carson Jenkins\n",
        "02/02/23\n",
        "This is a security program that runs through a series of questions, \n",
        "restarting the loop each time the user is incorrect, and revealing a \n",
        "secret after the user successfully answers all the questions in a row.\n",
        "'''\n",
        "import random\n",
        "incorrect = \"Incorrect, start over\"\n",
        "correct = \"Correct, continue\"\n",
        "# Initializing restart variable as false with a \"Falsey\" value\n",
        "restart = \"\"\n",
        "# \"Truthy\" value used for while loop\n",
        "while 1:\n",
        "  # Prompts user for side, and has them calculate area of either \n",
        "  # a square or triangle, restarts while loop if incorrect\n",
        "  while 1:\n",
        "    print(\"1. Square\\n2. Triangle\\n\")\n",
        "    area_choice = input(\"Which do you want the area for? \")\n",
        "    if area_choice == str(1):\n",
        "      side = input(\"Length of side: \")\n",
        "      area = int(side) * int(side)\n",
        "      area_answer = input(\"Compute area of square with side length \" + str(side) + \": \")\n",
        "      if int(area_answer) != area:\n",
        "        print(incorrect)\n",
        "        continue\n",
        "      break\n",
        "    elif area_choice == str(2):\n",
        "      base = input(\"Base of triangle: \")\n",
        "      height = input(\"Height of triangle: \")\n",
        "      # Float value used here\n",
        "      area = 0.5 * int(base) * int(height)\n",
        "      area_answer = input(\"Compute area of trangle with base \" + str(base) + \" and height \" + str(height) + \": \")\n",
        "      if int(area_answer) != area:\n",
        "        print(incorrect)\n",
        "        continue\n",
        "      break\n",
        "    else:\n",
        "      print(\"Error: enter either 1 or 2\")\n",
        "  # This for loop repeats 3 times, prompting the user with randomly \n",
        "  # generated equations. The second number is provided by the index, \n",
        "  # which is based on the randomized range values. 3 different \n",
        "  # operators are used based on index\n",
        "  rand_range = random.randint(1, 20)\n",
        "  for i in range(rand_range, rand_range+3):\n",
        "    first_number = random.randint(50, 100)\n",
        "    if i == rand_range:\n",
        "      mod_answer = input(str(first_number) + \" % \" + str(i) + \" = \")\n",
        "      correct = first_number % (i)\n",
        "    elif i == rand_range + 1:\n",
        "      mod_answer = input(str(first_number) + \" - \" + str(i) + \" = \")\n",
        "      correct = first_number - (i)\n",
        "    else:\n",
        "      print(\"Disregard decimal remainder: \")\n",
        "      mod_answer = input(str(first_number) + \" // \" + str(i) + \" = \")\n",
        "      correct = first_number // (i)\n",
        "    if int(mod_answer) != correct:\n",
        "      print(incorrect)\n",
        "      restart = True\n",
        "      break\n",
        "    else:\n",
        "      print(correct)\n",
        "  # Restarts the while loop if any answers were incorrect in the for loop\n",
        "  if restart:\n",
        "    continue\n",
        "  break\n",
        "# Last section displays secret passwords the program is leading you to unlock\n",
        "secrets = [\"jdajs998fd\", \"34neJnf34\", \"pswd145unlck23\", \"013003Uo\"]\n",
        "print(\"You completed the security quiz. Here are all of your passwords: \")\n",
        "for i in range(len(secrets)):\n",
        "  print(secrets[i])"
      ]
    }
  ]
}