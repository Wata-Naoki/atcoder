{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPHRM78xoXnWXhbbC4sjIuE",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC108A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EsMLN76vy4e-",
        "outputId": "e20e9025-a12b-493c-d579-b3899f1aea77"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11\n",
            "30\n"
          ]
        }
      ],
      "source": [
        "k = int(input())\n",
        "if k % 2 == 1:\n",
        "  a = (k-1)//2\n",
        "  b = (k+1)//2\n",
        "else:\n",
        "  a = k//2\n",
        "  b = k//2\n",
        "print(a*b)"
      ]
    }
  ]
}