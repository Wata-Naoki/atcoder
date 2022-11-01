{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNUjNmneaX9Rqk5mhVhBJY4",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC105B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input())\n",
        "\n",
        "flag = False\n",
        "\n",
        "for i in range(101):\n",
        "  for j in range(101):\n",
        "    if 100 < i + j or N < 4:\n",
        "      break\n",
        "    if 4 * i + 7 * j == N:\n",
        "      flag = True\n",
        "      continue\n",
        "    if flag:\n",
        "      break\n",
        "\n",
        "print('Yes' if flag else 'No')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a7LAYiGPxHrt",
        "outputId": "be750ddb-2bca-4a84-d90e-f1684a9b00a8"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11\n",
            "Yes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "1N = int(input())\n",
        "n = 0\n",
        "while n * 7 <= N:\n",
        "  if(N-n *7)%4==0:\n",
        "    print('Yes')\n",
        "    break\n",
        "  n += 1\n",
        "\n",
        "else:\n",
        "  print('No')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YSsPbRNyuikQ",
        "outputId": "8ebc0377-1767-4d89-a4ed-98b744551b6b"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11\n",
            "Yes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_Z--6ofTl-Zu"
      },
      "outputs": [],
      "source": [
        "n = int(input())\n",
        "\n",
        "\n",
        "\n",
        "if \n",
        "\n",
        "if n%4==0 or n%7==0 or n%11 == 0 or :\n",
        "  print('Yes')"
      ]
    }
  ]
}