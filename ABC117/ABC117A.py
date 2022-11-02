{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNTH/9L4dkFG3kDu/NFMzZ/",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC117A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "問題文\n",
        "明日の入学試験に合格するために、太郎くんはあと T 時間の勉強をする必要があります。\n",
        "\n",
        "幸いにも、彼は今いる世界(世界A)の X 倍の速度で時間が進む世界Bへ世界跳躍(ワールドリープ)することができます。\n",
        "\n",
        "世界Bで (X×t) 時間進むと、世界Aでは t 時間進みます。\n",
        "\n",
        "世界Bで T 時間勉強したとき、世界Aでは何時間進んでいるでしょうか。"
      ],
      "metadata": {
        "id": "oRbgoBCs8zaG"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "ZEBJ_lHQ4txo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0f684174-84c2-4696-ccf0-085891976614"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8 3\n",
            "2.6666666666666665\n"
          ]
        }
      ],
      "source": [
        "t, x=map(int,input().split())\n",
        "\n",
        "print(t/x)"
      ]
    }
  ]
}