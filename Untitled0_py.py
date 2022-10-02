{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOjZZDRw2L2Dn9p4h3goZT9",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/Untitled0_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K1vB9PoeVtPL",
        "outputId": "a8fa6f8f-fa8c-4584-9293-f1013664a1b4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 3\n",
            "7\n"
          ]
        }
      ],
      "source": [
        "a = int(input())\n",
        "\n",
        "b, c = map(int, input().split())\n",
        "\n",
        "s = input()\n",
        "\n",
        "print('{} {}'.format())"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a,b = map(int, input().split())\n",
        "\n",
        "c = a * b\n",
        "\n",
        "if c%2 == 0:\n",
        "  print('Even')\n",
        "\n",
        "elif c%2 == 1:\n",
        "  print('Odd')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u7BDqqHAfk2h",
        "outputId": "3cd947ab-079a-42fb-a871-c10a9312fce5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 3\n",
            "Odd\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a  = input()\n",
        "print(a.count('1'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Nb9b29s4hUrS",
        "outputId": "925f6e3a-57a6-4376-eabc-fb8327e36ba3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "101\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "l = list(map(int, input().split()))\n",
        "print(l)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PP-dFX6kxtW0",
        "outputId": "65bbb7fd-eea9-44be-b0bd-53ea28815e3f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 4\n",
            "[1, 2, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input())\n",
        "l = list(map(int, input().split()))\n",
        " \n",
        "flag = 0\n",
        "k = 0\n",
        " \n",
        "while True:\n",
        "  for i in range(n):\n",
        "    if l[i]%2 != 0:\n",
        "      flag = 1\n",
        "  if flag == 1:\n",
        "    break\n",
        "  for i in range (n):\n",
        "    l[i] = l[i] // 2\n",
        "  k += 1\n",
        "    \n",
        "print(k)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Pcbk5nWKzf0d",
        "outputId": "e3cf50c3-9747-45db-bd9b-dbb51d0aa32d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "8 12 40\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "kvhUheOaQSPA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "A = int(input())\n",
        "B = int(input())\n",
        "C = int(input())\n",
        "X = int(input())\n",
        "\n",
        "count=0\n",
        "total_num = 0\n",
        "for a in range(A+1):\n",
        "  for b in range(B+1):\n",
        "    for c in range(C+1):\n",
        "      total_num = 500*a+100*b+50*c\n",
        "      if total_num==X:\n",
        "        count+=1\n",
        "print(count)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K6no2W5nMZko",
        "outputId": "23424f68-9e4c-4a89-d002-f8da6a19af50"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "2\n",
            "2\n",
            "100\n",
            "0\n",
            "50\n",
            "100\n",
            "100\n",
            "150\n",
            "200\n",
            "200\n",
            "250\n",
            "300\n",
            "500\n",
            "550\n",
            "600\n",
            "600\n",
            "650\n",
            "700\n",
            "700\n",
            "750\n",
            "800\n",
            "1000\n",
            "1050\n",
            "1100\n",
            "1100\n",
            "1150\n",
            "1200\n",
            "1200\n",
            "1250\n",
            "1300\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。\n",
        "\n",
        "N, A, B = list(map(int, input().split()))\n",
        "\n",
        "sum_all = 0\n",
        "\n",
        "for number in range(1, N+1):\n",
        "\n",
        "  sum_number = 0\n",
        "  for i in str(number):\n",
        "    sum_number += int(i)\n",
        "\n",
        "  if sum_number >= A and sum_number <= B:\n",
        "    sum_all += number\n",
        "\n",
        "\n",
        "print(sum_all)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ERfl0M-TQUXH",
        "outputId": "fc5362d6-1421-4f7c-be22-3be60e4437f2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20 2 5\n",
            "1\n",
            "1\n",
            "2\n",
            "2\n",
            "2\n",
            "3\n",
            "3\n",
            "5\n",
            "4\n",
            "4\n",
            "9\n",
            "5\n",
            "5\n",
            "14\n",
            "6\n",
            "6\n",
            "7\n",
            "7\n",
            "8\n",
            "8\n",
            "9\n",
            "9\n",
            "10\n",
            "10\n",
            "10\n",
            "11\n",
            "11\n",
            "11\n",
            "25\n",
            "12\n",
            "12\n",
            "12\n",
            "37\n",
            "13\n",
            "13\n",
            "13\n",
            "50\n",
            "14\n",
            "14\n",
            "14\n",
            "64\n",
            "15\n",
            "15\n",
            "15\n",
            "16\n",
            "16\n",
            "16\n",
            "17\n",
            "17\n",
            "17\n",
            "18\n",
            "18\n",
            "18\n",
            "19\n",
            "19\n",
            "19\n",
            "20\n",
            "20\n",
            "20\n",
            "84\n",
            "84\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# N 枚のカードがあります. i 枚目のカードには, a iという数が書かれています.\n",
        "# Alice と Bob は, これらのカードを使ってゲームを行います. ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. Alice が先にカードを取ります.\n",
        "# 2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.\n",
        "\n",
        "\n",
        "N = int(input())\n",
        "list = list(map(int, input().split()))\n",
        "\n",
        "list.sort(reverse=True)\n",
        "\n",
        "A = 0\n",
        "B = 0\n",
        "\n",
        "for index, item in enumerate(list):\n",
        "  if index%2==0:\n",
        "    A += item\n",
        "  elif index%2==1:\n",
        "    B += item\n",
        "\n",
        "print(A-B)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wHk2woL9c1k6",
        "outputId": "6f222949-c3bb-406c-e9dc-84f18d80c16f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "2 7 4\n",
            "5\n"
          ]
        }
      ]
    }
  ]
}