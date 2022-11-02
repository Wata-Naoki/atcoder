{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO+nVUA60VbAF6+R8tFJK8/",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC113B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "dd_Z7Fa5W7YX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a1ee1b8b-3b52-447a-84aa-48a8b1d2e706"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "12 5\n",
            "1000\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "n = int(input())\n",
        "t, a = map(int, input().split())\n",
        "ans, at = 0, float('inf')\n",
        "for i, h in enumerate(map(int, input().split())):\n",
        "    tt = abs(t - h * 0.006 - a)\n",
        "    if at > tt:\n",
        "        ans = i + 1\n",
        "        at = tt\n",
        "print(ans)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ERZk-0P0fEEU"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}