{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOgWkcV1GXA1ubOWqVlhedG",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC111B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lVlaijMuImKI",
        "outputId": "59dd329b-9be4-4ad2-d2d7-b7d630697382"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "750\n",
            "777\n"
          ]
        }
      ],
      "source": [
        "n = int(input())\n",
        "\n",
        "ans = 0\n",
        "\n",
        "for i in range(1, 10):\n",
        "  # print(i*111)\n",
        "  if n <= 111:\n",
        "    print(111)\n",
        "    break\n",
        "  if n > i * 111 and n <= (i +1)* 111:\n",
        "    print((i +1)* 111)\n",
        "    break\n",
        "\n"
      ]
    }
  ]
}