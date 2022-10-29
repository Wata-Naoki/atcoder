{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKchJKQV47nBkumip7eVkS",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC119B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sYbqxKr4Xr-6",
        "outputId": "1b27a2f0-057b-4aa2-d8a3-5b42985b08fc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "10000 JPY\n",
            "10000 JPY\n",
            "0.10000000 BTC\n",
            "0.10000000 BTC\n",
            "38000.0\n",
            "48000.0\n"
          ]
        }
      ],
      "source": [
        "n=int(input())\n",
        "\n",
        "count=0\n",
        "\n",
        "for i in range(n):\n",
        "  a, b =map(str, input().split())\n",
        "  #print(a, b)\n",
        "  if b==\"BTC\":\n",
        "    a = float(a)*380000\n",
        "    #print(a)\n",
        "  count +=float(a)\n",
        "\n",
        "print(count)\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = '123'\n",
        "\n",
        "a = int(a)\n",
        "\n",
        "print(a)\n",
        "\n",
        "#123\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KIzuS4X2doyQ",
        "outputId": "0a19f4f0-b86b-4954-de60-48b47b096097"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "123\n"
          ]
        }
      ]
    }
  ]
}