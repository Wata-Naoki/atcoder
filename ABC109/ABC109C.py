{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMXE+WO8kdh8vu7n9sr/Twj",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC109C.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "i4JMpiGSR8Ge"
      },
      "outputs": [],
      "source": [
        "from fractions import gcd\n",
        " \n",
        "n, s = map(int, input().split())\n",
        "xxx = [abs(s - y) for y in map(int, input().split())]\n",
        "d = xxx[0]\n",
        "for x in xxx[1:]:\n",
        "    d = gcd(d, x)\n",
        "print(d)\n",
        "\n",
        "# absで絶対値で各都市の差を求める\n",
        "# xxx[1:]で配列のindex1番以降の数を順にxに入れる\n",
        "# gcdでxxxのlistの最初の値と配列のindex1番以降の数のそれぞれの2つの最大公約数を求める"
      ]
    }
  ]
}