<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>My booklet Collection</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Name</th>
      <th>Place</th>
      <th>Price </th>
    </tr>
    <xsl:for-each select="booklet/concert_ad">
		  <xsl:if test="price &gt; 100">
        <xsl:choose>
          <xsl:when test="month/@type = 'a' ">
        <xsl:choose>
          <xsl:when test="place/@type = 'm' ">

          <xsl:choose>
          <xsl:when test="discount/@type = 'yes'">
            <tr style="background-color:#00cc00">
            <td><xsl:value-of select="name"/></td>
            <td><xsl:value-of select="place"/></td>
            <td><xsl:value-of select="price"/></td>
            </tr>
          </xsl:when>
          <xsl:otherwise>
          <tr>
            <td><xsl:value-of select="name"/></td>
            <td><xsl:value-of select="place"/></td>
            <td><xsl:value-of select="price"/></td>
          </tr>
        </xsl:otherwise>

        </xsl:choose>
        </xsl:when>
      </xsl:choose>
    </xsl:when>
  </xsl:choose>
      </xsl:if>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet> 