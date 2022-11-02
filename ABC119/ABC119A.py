{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNyAWMWTOBZhsH+Ei5kVOzN",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC119A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "P5dg29hWKAWT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d2a2831b-13cc-4322-cd7c-b6bc07155d0c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2019/11/01\n",
            "TBD\n"
          ]
        }
      ],
      "source": [
        "s=input()\n",
        "\n",
        "if 2019==int(s[:4]) and 4>=int(s[5:7]) and 30>=int(s[-2:]):\n",
        "  # print(int(s[:3]), int(s[5:7]), int(s[-2:]))\n",
        "  print('Heisei')\n",
        "\n",
        "elif 2019 > int(s[:4]):\n",
        "  # print(int(s[:4]))\n",
        "  print('Heisei')\n",
        "\n",
        "else:\n",
        "  print('TBD')\n",
        "  "
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s=\"01\"\n",
        "\n",
        "print(int(s))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_7858B1_Reak",
        "outputId": "f0ce9697-c155-4da6-fdf7-3a1e4225f4bc"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    }
  ]
}