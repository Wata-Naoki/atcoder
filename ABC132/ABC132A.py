{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPRydosPNRyVPQPE6cSGGqo",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC132A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-5WMRDqPRRQK",
        "outputId": "973d7ade-6943-4963-ae67-8349c7059797"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "FREE\n",
            "No\n"
          ]
        }
      ],
      "source": [
        "s=list(input())\n",
        "count=0\n",
        "\n",
        "for i, v in enumerate(s[2:]):\n",
        "  if s[0] == v or s[1] ==v:\n",
        "    count+=1\n",
        "\n",
        "print('Yes' if count==2 else 'No')\n",
        "  \n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s=input()\n",
        "\n",
        "a=set()\n",
        "for i in range(len(s)):\n",
        "  a.add(s[i])\n",
        "\n",
        "print('Yes' if len(a)==2 else 'No')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dEUGcrCSTjiP",
        "outputId": "b9f2ef9e-c97c-4f61-d559-306629f45728"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "FFEE\n",
            "Yes\n"
          ]
        }
      ]
    }
  ]
}