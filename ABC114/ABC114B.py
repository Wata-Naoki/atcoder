{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOZlD7Vv/OZtNmy4dPHSvei",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC114B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "sw1_gNaMk6Hi",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ae3f8db3-2a3b-4d8f-c1f6-6c55fcee3da9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "35753\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "s=input()\n",
        "\n",
        "ans_list=[]\n",
        "\n",
        "for i in range(len(s)-2):\n",
        "  ans = abs(753- int(s[i:3+i]))\n",
        "  # if ans==0:\n",
        "  #   print(0)\n",
        "  #   break\n",
        "  ans_list.append(ans)\n",
        "  \n",
        "\n",
        "print(min(ans_list))\n",
        "\n",
        "  "
      ]
    }
  ]
}