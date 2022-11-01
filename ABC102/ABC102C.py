{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNkkPRn6xcqQAzETKIdN9RC",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC102C.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from statistics import median\n",
        "\n",
        "n = int(input())\n",
        "\n",
        "# 各要素を配列の中に入れる\n",
        "xs =[int(x) for x in input().split()]\n",
        "# print(xs)\n",
        "\n",
        "# 配列の各要素に-i -1をする\n",
        "# b+1はBのすべての要素に1ずつ近くなる\n",
        "# bがBの最小の要素と同じ値だったとする（Bの最小の要素が単一だと仮定する）。\n",
        "# するとb+1はその最小の要素からの距離は1増え、n-1個の要素との距離は1ずつ減る。\n",
        "# とにかく、配列の真ん中の値が一番距離が近くなるのでそれを求める\n",
        "ys = [x-i-1 for i, x in enumerate(xs)]\n",
        "# print(ys)\n",
        "m = int(median(ys))\n",
        "# print(m)\n",
        "\n",
        "print(sum(abs(y-m) for y in ys))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jRLCYAq4J4bd",
        "outputId": "cafd0326-22a7-4a29-f85c-fa12b9813b6c"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n",
            "6 5 4 3 2 1\n",
            "[6, 5, 4, 3, 2, 1]\n",
            "[5, 3, 1, -1, -3, -5]\n",
            "0\n",
            "18\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "kykXPhVBLN6i"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CqkdO4op_t1o",
        "outputId": "65252a1a-9070-4c49-d22d-6898178dccf1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n",
            "6 5 4 3 2 1\n",
            "18\n"
          ]
        }
      ],
      "source": [
        "n = int(input())\n",
        "a_list = list(map(int, input().split()))\n",
        "\n",
        "ans = 0\n",
        "num = 0\n",
        "\n",
        "for i in range(1, n+1):\n",
        "  ans += abs(a_list[num] - (0+i))\n",
        "  num += 1\n",
        "\n",
        "# for index, a in enumerate(a_list):\n",
        "#   index += 1\n",
        "#   ans += abs(a-(0+(index+1)))\n",
        "#   print(ans)\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}