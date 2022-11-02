{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPjNE3jCsle1gM5VxR2E/Gt",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC111A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sglt8BCdEAXK",
        "outputId": "50fd561d-bd70-46af-a0d4-0a40f6b2d712"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "119\n",
            "991\n"
          ]
        }
      ],
      "source": [
        "n = input()\n",
        "\n",
        "tras_1 = n.replace('1', 'z')\n",
        "trans_9 = tras_1.replace('9', 'x')\n",
        "ans = trans_9.replace('z', '9').replace('x', '1')\n",
        "print(ans)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# n = input()\n",
        "\n",
        "# s = n.replace('1', '9').replace('9', '1')\n",
        "# print(s)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FgKw6zqvGxCL",
        "outputId": "abe8e4f0-ce02-4c8c-f825-2675a81b3c41"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "991\n",
            "111\n"
          ]
        }
      ]
    }
  ]
}