{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN+LHTHNY06NjSs0QMh6Xku",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC142B.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G3GQi9jYK0sm",
        "outputId": "c9f2da5c-47d5-4ef7-ec3b-f275c2df0121"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 150\n",
            "150 150\n",
            "2\n"
          ]
        }
      ],
      "source": [
        "n,k=map(int, input().split())\n",
        "h_list=[int(h) for h in input().split()]\n",
        "# print(n,k,h_list)\n",
        "count=0\n",
        "\n",
        "for h in h_list:\n",
        "  if k <= h:\n",
        "    count+=1\n",
        "print(count)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Y-1ZFPo_Msvz"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}