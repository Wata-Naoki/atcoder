{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNLpYBXTBsNydLrs934NU/H",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC127B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dSbx5pM1k5Qy",
        "outputId": "18a0bbd2-a8d1-4764-8bdf-db69f449e9a0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 10 20\n",
            "30\n",
            "50\n",
            "90\n",
            "170\n",
            "330\n",
            "650\n",
            "1290\n",
            "2570\n",
            "5130\n",
            "10250\n"
          ]
        }
      ],
      "source": [
        "n, m, k =map(int, input().split())\n",
        "\n",
        "for i in range(10):\n",
        "  k = (n*k) - m\n",
        "  print(k)\n",
        "\n"
      ]
    }
  ]
}