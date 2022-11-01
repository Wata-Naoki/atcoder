{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPWwiwl6XnqaC8LZ2HYykV7",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC101B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3zuSoBUn7P9U",
        "outputId": "f1704e7a-510b-48d2-953b-20792cb1deaf"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "101\n",
            "No\n"
          ]
        }
      ],
      "source": [
        "N= (int(input()))\n",
        "N_2 = list(str(N))\n",
        "\n",
        "total_count = 0\n",
        "\n",
        "for num in N_2:\n",
        "  total_count += int(num)\n",
        "\n",
        "if N%total_count==0:\n",
        "  print('Yes')\n",
        "else:\n",
        "  print('No')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = input()\n",
        "num = 0\n",
        " \n",
        "for i in range(len(n)):\n",
        "  num += int(n[i])\n",
        " \n",
        "n = int(n)\n",
        " \n",
        "print(\"Yes\" if n%num==0 else \"No\")\n",
        "\n",
        "\n",
        "# こっちの方がいいかも。nを最初にstrの形で受け取って、繰り返しの時にn（文字列）のi番目を整数化するやり方\n"
      ],
      "metadata": {
        "id": "KUYnNPkq_BED"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "rjGRDa65_BNI"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}