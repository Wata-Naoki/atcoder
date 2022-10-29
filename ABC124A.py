{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOdgk3NOLEZuO/zfbigRIrK",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC124A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a, b=map(int, input().split())\n",
        "\n",
        "ans=0\n",
        "for i in range(2):\n",
        "  if a>b:\n",
        "    ans+=a\n",
        "    a -= 1\n",
        "  else:\n",
        "    ans+=b\n",
        "    b -= 1\n",
        "\n",
        "print(ans)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jyrda6IjCBSt",
        "outputId": "44e3cbc5-7725-40ae-baeb-af21fe6d5714"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6 6\n",
            "12\n"
          ]
        }
      ]
    }
  ]
}