{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMnaFCOHPUdkr+yzHpDEPIy",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC120B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lpufUigErJJh",
        "outputId": "822c8f59-5b29-4bbb-d51e-6e35962da3c6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 50 4\n",
            "[50, 25, 10, 5, 2, 1]\n",
            "5\n"
          ]
        }
      ],
      "source": [
        "a,b,k=map(int, input().split())\n",
        "\n",
        "ans_list=[]\n",
        "i=1\n",
        "count=0\n",
        "while i<=a and i<=b:\n",
        "  if a%i==0 and b%i==0:\n",
        "    ans_list.append(i)\n",
        "  i +=1\n",
        "\n",
        "ans_list.sort(reverse=True)\n",
        "\n",
        "# print(ans_list)\n",
        "print(ans_list[k-1])"
      ]
    }
  ]
}