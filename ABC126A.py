{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPITk71bdM+Y+DhLiTtkOzj",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC126A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "R35pTvIwEaCn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6928bb7a-1d68-47ba-9ae5-8546ce0a47e6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 1\n",
            "ABC\n",
            "aBC\n"
          ]
        }
      ],
      "source": [
        "N, K = map(int,input().split())\n",
        "S = input()\n",
        "print(S[:K-1] + S[K-1].lower() + S[K:])"
      ]
    }
  ]
}