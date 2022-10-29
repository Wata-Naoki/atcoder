{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/k4QX8gIuVLGj8VqwyIeb",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC118B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8MdAj9zdaJEh",
        "outputId": "a144318f-0493-48a1-b23c-2ebf88f4d8fc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 4\n",
            "2 1 3\n",
            "[1]\n",
            "[1, 3]\n",
            "3 1 2 3\n",
            "[1, 3, 1]\n",
            "[1, 3, 1, 2]\n",
            "[1, 3, 1, 2, 3]\n",
            "2 3 2\n",
            "[1, 3, 1, 2, 3, 3]\n",
            "[1, 3, 1, 2, 3, 3, 2]\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "n, m=map(int, input().split())\n",
        "\n",
        "l=[]\n",
        "\n",
        "for i in range(n):\n",
        "  a = [int(x) for x in input().split()]\n",
        "  for j in range(1, a[0] + 1):\n",
        "    l.append(a[j])\n",
        "                                                                                     \n",
        "ans=0\n",
        "\n",
        "for i in range(m+1):\n",
        "  if l.count(i)==n:\n",
        "\n",
        "    ans +=1\n",
        "\n",
        "print(ans)      \n",
        "    \n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "  # n,m=map(int, input().split())\n",
        "\n",
        "  # ans_list=[]\n",
        "\n",
        "  # for i in range(n):\n",
        "  #   list_a=list(map(int, input().split()))\n",
        "  #   ans_list.append(list_a)\n",
        "\n",
        "\n",
        "  # total=0\n",
        "  # count=0\n",
        "  # for k in range(n):\n",
        "  #   for j in range(1, 31):\n",
        "  #     if j in ans_list[k][1:]:\n",
        "  #       count +=1\n",
        "        \n",
        "\n",
        "  # if count==n:\n",
        "  #     total += 1\n",
        "    \n",
        "\n"
      ],
      "metadata": {
        "id": "bUTiaG2pjkPX"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a=[[1,2], [3,4]]\n",
        "print(a[:\n",
        "        ][1:])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zHUilltWoppj",
        "outputId": "f211ab12-600e-476b-8192-346f9c7e55dc"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=[1, 2, 3]\n",
        "\n",
        "if 1 in a and 2 in a and 9 in a:\n",
        "  print(True)\n",
        "else:\n",
        "  print(False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LVpplLsCg7N6",
        "outputId": "8e486453-07d3-4063-8002-67350e565de5"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    }
  ]
}