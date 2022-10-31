{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP4Q7qqTD8bXdWFAKS4o5cc",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC132B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "Y5lW0NmReiV_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "df299a89-aa1a-4adc-dbf3-c12fd14fe347"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9\n",
            "9 6 3 2 5 8 7 4 1\n",
            "[9, 6, 3, 2, 5, 8, 7, 4, 1]\n",
            "\n",
            "[9, 6, 3] [3, 6, 9]\n",
            "[6, 3, 2] [2, 3, 6]\n",
            "[3, 2, 5] [2, 3, 5]\n",
            "[2, 5, 8] [2, 5, 8]\n",
            "[5, 8, 7] [5, 7, 8]\n",
            "[8, 7, 4] [4, 7, 8]\n",
            "[7, 4, 1] [1, 4, 7]\n",
            "[4, 1] [1, 4]\n",
            "終了\n",
            "5\n"
          ]
        }
      ],
      "source": [
        "n=int(input())\n",
        "\n",
        "s=[int(x) for x in input().split()]\n",
        "count=0\n",
        "\n",
        "for i in range(n):\n",
        "  s_list=s[i:3+i]\n",
        "  tmp_list=s[i:3+i]\n",
        "  \n",
        "  tmp_list.sort()\n",
        "  \n",
        "  # print(s[i:3+i], tmp_list)\n",
        "  if len(s[i:3+i]) <3:\n",
        "    # print('終了')\n",
        "    break\n",
        "  else:\n",
        "    if s_list[1] is tmp_list[1]:\n",
        "      count+=1\n",
        "\n",
        "print(count)\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}