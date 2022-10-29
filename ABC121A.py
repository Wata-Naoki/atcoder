{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "view-in-github"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC121A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rLg2QMmR6TCZ",
        "outputId": "9e25cdf4-b53c-4e23-edd3-0c32f8896364"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "3 2\n",
            "2 1\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "H, W=map(int, input().split())\n",
        "h,w=map(int, input().split())\n",
        "\n",
        "print((H-h)*(W-w))"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "authorship_tag": "ABX9TyNqKwLyE77BAbTYJdHiYoUT",
      "include_colab_link": true,
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3.9.6 64-bit",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.9.6"
    },
    "vscode": {
      "interpreter": {
        "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
