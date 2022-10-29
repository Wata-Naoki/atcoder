{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNRyl/NrmuJX/GbAa40pWXx",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC122B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "jooGHcwiMiRl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "24c17c9b-e04e-462e-fb71-ef5acec6c59b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ATCODE R\n",
            "['A', 'T', 'C', 'O', 'D', 'E', 'R']\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "S = input()\n",
        "ACGT = ['A', 'C', 'G', 'T']\n",
        " \n",
        "ans = 0\n",
        "tmp = 0\n",
        "for i in range(len(S)):\n",
        "    if S[i] in ACGT:\n",
        "        tmp += 1\n",
        "        ans = max(tmp, ans)\n",
        "    else:\n",
        "        tmp = 0\n",
        " \n",
        "print(ans)"
      ]
    }
  ]
}