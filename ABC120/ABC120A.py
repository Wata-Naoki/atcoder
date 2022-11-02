{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOsrM8/czAHD9+iEobjqyRv",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC120A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YFuDErzplP5F",
        "outputId": "b9471e45-9145-4424-c015-b756e70b466c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 1 10\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "a,b,c=map(int, input().split())\n",
        "ans=0\n",
        "if a*c<=b:\n",
        "  print(c)\n",
        "else:\n",
        "  ans=b//a\n",
        "  print(ans)\n"
      ]
    }
  ]
}