{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM4uERGpRL2wTypIAEf9e0z",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC106C.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fzPlEPwpsT6o",
        "outputId": "e186e85f-c5c1-49a5-eeab-ef78dbcf7562"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "299792458\n",
            "9460730472580800\n",
            "2\n"
          ]
        }
      ],
      "source": [
        "s = input()\n",
        "k = int(input()) -1\n",
        "# k=1文字目は文字列sの0番目なので-1。enumerateは文字列を1つずつ出す処理\n",
        "for i, c in enumerate(s):\n",
        "  if i == k:\n",
        "    print(c)\n",
        "    break\n",
        "  if c != '1':\n",
        "    print(c)\n",
        "    break"
      ]
    }
  ]
}