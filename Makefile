# Makefile for source rpm: net-tools
# $Id$
NAME := net-tools
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
